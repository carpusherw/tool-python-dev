"""Sign JWT tokens."""

import argparse
import datetime
import sys

import jwt


def sign_jwt(
    private_key_id: str,
    private_key_pem: str,
    issuer: str = "svc-test",
    subject: str = "svc-test",
    name: str = "Sample User",
    days: int = 1,
) -> str:
    """
    Sign a JWT token with the given parameters.

    Args:
        private_key_id: Private key ID (kid) to use in JWT header.
        private_key_pem: Private key PEM content.
        issuer: Token issuer.
        subject: Token subject.
        name: Name claim.
        days: Token expiration in days.

    Returns:
        Signed JWT token string.
    """
    payload = {
        "iss": issuer,
        "sub": subject,
        "name": name,
        "exp": datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(days=days),
    }

    token = jwt.encode(
        payload,
        private_key_pem,
        headers={
            "kid": private_key_id,
            "alg": "ES512",
        },
        algorithm="ES512",
    )

    return token


def main() -> int:
    """Main entry point for the sign_jwt tool."""
    parser = argparse.ArgumentParser(description="Sign JWT token")
    parser.add_argument("private_key_id", help="Private key ID (kid) to use in JWT header")
    parser.add_argument("private_key_file", help="Path to private key PEM file")
    parser.add_argument("--issuer", default="svc-test", help="Token issuer (default: svc-test)")
    parser.add_argument("--subject", default="svc-test", help="Token subject (default: svc-test)")
    parser.add_argument("--name", default="Sample User", help="Name claim (default: Sample User)")
    parser.add_argument("--days", type=int, default=1, help="Token expiration in days (default: 1)")

    args = parser.parse_args()

    try:
        with open(args.private_key_file) as f:
            private_key_pem = f.read()
    except FileNotFoundError:
        print(f"Error: Private key file '{args.private_key_file}' not found")
        return 1
    except Exception as e:
        print(f"Error reading private key file: {e}")
        return 1

    token = sign_jwt(
        private_key_id=args.private_key_id,
        private_key_pem=private_key_pem,
        issuer=args.issuer,
        subject=args.subject,
        name=args.name,
        days=args.days,
    )

    print(token)
    return 0


if __name__ == "__main__":
    sys.exit(main())
