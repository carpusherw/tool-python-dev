"""Unit tests for the sign_jwt tool."""

import datetime

import jwt
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ec

from sign_jwt import sign_jwt


def generate_ec_key_pair() -> tuple[str, str]:
    """Generate an EC key pair for testing."""
    private_key = ec.generate_private_key(ec.SECP521R1())
    private_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption(),
    ).decode()
    public_pem = (
        private_key.public_key()
        .public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo,
        )
        .decode()
    )
    return private_pem, public_pem


def test_sign_jwt_default_values():
    """Test sign_jwt with default values."""
    private_pem, public_pem = generate_ec_key_pair()

    token = sign_jwt(
        private_key_id="test-key-id",
        private_key_pem=private_pem,
    )

    decoded = jwt.decode(token, public_pem, algorithms=["ES512"])

    assert decoded["iss"] == "svc-test"
    assert decoded["sub"] == "svc-test"
    assert decoded["name"] == "Sample User"
    assert decoded["tenant"] == "localhost"
    assert "exp" in decoded


def test_sign_jwt_custom_values():
    """Test sign_jwt with custom values."""
    private_pem, public_pem = generate_ec_key_pair()

    token = sign_jwt(
        private_key_id="custom-key-id",
        private_key_pem=private_pem,
        issuer="custom-issuer",
        subject="custom-subject",
        name="Custom Name",
        tenant="custom-tenant",
        days=7,
    )

    decoded = jwt.decode(token, public_pem, algorithms=["ES512"])

    assert decoded["iss"] == "custom-issuer"
    assert decoded["sub"] == "custom-subject"
    assert decoded["name"] == "Custom Name"
    assert decoded["tenant"] == "custom-tenant"


def test_sign_jwt_header_contains_kid():
    """Test that JWT header contains the correct kid."""
    private_pem, _ = generate_ec_key_pair()

    token = sign_jwt(
        private_key_id="my-key-id",
        private_key_pem=private_pem,
    )

    header = jwt.get_unverified_header(token)

    assert header["kid"] == "my-key-id"
    assert header["alg"] == "ES512"


def test_sign_jwt_expiration():
    """Test that JWT expiration is set correctly."""
    private_pem, public_pem = generate_ec_key_pair()

    token = sign_jwt(
        private_key_id="test-key-id",
        private_key_pem=private_pem,
        days=3,
    )

    decoded = jwt.decode(token, public_pem, algorithms=["ES512"])
    exp_datetime = datetime.datetime.fromtimestamp(
        decoded["exp"], tz=datetime.timezone.utc
    )
    now = datetime.datetime.now(datetime.timezone.utc)

    # Expiration should be approximately 3 days from now (within a few seconds tolerance)
    delta = exp_datetime - now
    assert 2 <= delta.days <= 3
