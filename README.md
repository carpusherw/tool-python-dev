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
