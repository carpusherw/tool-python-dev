# tool-python-dev

A collection of helper tools for development teams, powered by [uv](https://github.com/astral-sh/uv).

## What is this?

This project provides command-line helper tools that you can run instantly using `uvx` without needing to install them. Perfect for development teams who want to share useful utilities without managing complex installations.

## Quick Start

### Prerequisites

You only need [uv](https://github.com/astral-sh/uv) installed on your system.

### Using the Tools

#### From GitHub (SSH)

You can run tools directly from this GitHub repository using SSH authentication:

```bash
uvx --from git+ssh://git@github.com/carpusherw/tool-python-dev.git <tool_name> [arguments]
```

## Available Tools

- [sign_jwt](#sign_jwt) - Sign JWT tokens using ES512 algorithm

### sign_jwt

Sign JWT tokens using ES512 algorithm.

**Usage:**

```bash
uvx --from git+ssh://git@github.com/carpusherw/tool-python-dev.git sign_jwt <private_key_id> <private_key_file> [options]
```

**Arguments:**

- `private_key_id` - Private key ID (kid) to use in JWT header
- `private_key_file` - Path to private key PEM file

**Options:**

- `--issuer` - Token issuer (default: svc-test)
- `--subject` - Token subject (default: svc-test)
- `--name` - Name claim (default: Sample User)
- `--days` - Token expiration in days (default: 1)

**Examples:**

```bash
# Sign with default values
uvx --from git+ssh://git@github.com/carpusherw/tool-python-dev.git sign_jwt my-key-id ./private_key.pem

# Sign with custom values
uvx --from git+ssh://git@github.com/carpusherw/tool-python-dev.git sign_jwt my-key-id ./private_key.pem --issuer my-service --subject user@example.com --days 7
```

## For Developers

Want to contribute or add your own tools? Check out [AGENTS.md](AGENTS.md) for the complete development guide.
