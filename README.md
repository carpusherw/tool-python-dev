# tool-python-dev

A collection of helper tools for development teams, powered by [uv](https://github.com/astral-sh/uv).

## What is this?

This project provides command-line helper tools that you can run instantly using `uvx` without needing to install them. Perfect for development teams who want to share useful utilities without managing complex installations.

## Quick Start

### Prerequisites

You only need [uv](https://github.com/astral-sh/uv) installed on your system:

```bash
# On macOS and Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Or using pip
pip install uv

# Or using pipx
pipx install uv
```

### Using the Tools

#### From the Local Repository

If you've cloned this repository:

```bash
# Run the hello tool
uvx --from . hello

# Pass arguments to the tool
uvx --from . hello "World"
```

#### From PyPI (when published)

Once published, you can run tools without cloning:

```bash
# Run directly from PyPI
uvx tool-python-dev hello

# With arguments
uvx tool-python-dev hello "Developer"
```

## Available Tools

### hello

A simple greeting tool to demonstrate the project structure.

**Usage:**
```bash
# Default greeting
uvx --from . hello
# Output: Hello, World!

# Custom greeting
uvx --from . hello "Alice"
# Output: Hello, Alice!
```

**Examples:**
```bash
uvx --from . hello "Team"
# Output: Hello, Team!

uvx --from . hello "Development Team"
# Output: Hello, Development Team!
```

## For Developers

Want to contribute or add your own tools? Check out [AGENTS.md](AGENTS.md) for the complete development guide.

### Quick Development Setup

```bash
# Clone the repository
git clone https://github.com/carpusherw/tool-python-dev.git
cd tool-python-dev

# Install dependencies
uv sync

# Run tests
uv run pytest tests/

# Run tools locally
uv run hello
```

## Why uv and uvx?

- **Fast**: uv is 10-100x faster than pip
- **No installation needed**: uvx runs tools in isolated environments
- **Reproducible**: Lock file ensures consistent dependencies
- **Modern**: Built with Rust for performance and reliability

## Project Structure

```
tool-python-dev/
├── src/tool_python_dev/    # Source code for tools
├── tests/                  # Unit tests
├── pyproject.toml          # Project configuration
├── README.md               # This file (user guide)
└── AGENTS.md               # Development/contribution guide
```

## Contributing

Contributions are welcome! Please see [AGENTS.md](AGENTS.md) for detailed instructions on:
- Setting up your development environment
- Adding new tools
- Running tests
- Code style guidelines
- Submitting pull requests

## License

This project is open source. Please check the LICENSE file for details.

## Support

- **Documentation**: [AGENTS.md](AGENTS.md)
- **Issues**: [GitHub Issues](https://github.com/carpusherw/tool-python-dev/issues)
- **uv Documentation**: https://docs.astral.sh/uv/

## About uv

uv is an extremely fast Python package installer and resolver, written in Rust. It's designed as a drop-in replacement for pip, pip-tools, and virtualenv, with significantly better performance.

Learn more: https://github.com/astral-sh/uv