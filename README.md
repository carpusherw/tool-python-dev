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
# Run the hello tool
uvx --from git+ssh://git@github.com/carpusherw/tool-python-dev.git hello

# Pass arguments to the tool
uvx --from git+ssh://git@github.com/carpusherw/tool-python-dev.git hello "Developer"
```

## Available Tools

### hello

A simple greeting tool to demonstrate the project structure.

**Usage:**
```bash
# Default greeting
uvx --from git+ssh://git@github.com/carpusherw/tool-python-dev.git hello
# Output: Hello, World!

# Custom greeting
uvx --from git+ssh://git@github.com/carpusherw/tool-python-dev.git hello "Alice"
# Output: Hello, Alice!
```

**Examples:**
```bash
uvx --from git+ssh://git@github.com/carpusherw/tool-python-dev.git hello "Team"
# Output: Hello, Team!

uvx --from git+ssh://git@github.com/carpusherw/tool-python-dev.git hello "Development Team"
# Output: Hello, Development Team!
```

## For Developers

Want to contribute or add your own tools? Check out [AGENTS.md](AGENTS.md) for the complete development guide.

### Quick Development Setup

```bash
# Clone the repository
git clone git@github.com:carpusherw/tool-python-dev.git
cd tool-python-dev

# Install dependencies
uv sync

# Run tests
uv run pytest src/tests/

# Run tools locally
uv run hello
```

## Project Structure

```
tool-python-dev/
├── src/
│   ├── hello.py              # Hello world helper tool
│   └── tests/
│       └── test_hello.py     # Unit tests
├── pyproject.toml            # Project configuration
├── README.md                 # This file (user guide)
└── AGENTS.md                 # Development/contribution guide
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