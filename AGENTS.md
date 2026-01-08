# Contributing to tool-python-dev

This guide explains how to work with this repository, whether you're a human developer or a coding agent.

## Project Overview

This is a uv-based Python project that provides helper tools for development teams. The tools can be run using `uvx` without requiring installation.

## Prerequisites

- Python 3.14 or higher
- [uv](https://github.com/astral-sh/uv) - Fast Python package installer and resolver

## Getting Started

### Clone and Setup

```bash
# Clone the repository
git clone https://github.com/carpusherw/tool-python-dev.git
cd tool-python-dev

# Install dependencies
uv sync

# Run tests
uv run pytest
```

### Project Structure

```text
tool-python-dev/
├── src/
│   ├── hello.py              # Hello world helper tool
│   └── tests/
│       └── test_hello.py     # Unit tests
├── pyproject.toml            # Project configuration
├── README.md                 # User documentation
├── AGENTS.md                 # This file
└── CLAUDE.md                 # Symlink to AGENTS.md
```

## Development Workflow

### Adding a New Tool

1. Create a new module in `src/`:

   ```python
   # src/my_tool.py
   def main() -> None:
       """Main entry point for the tool."""
       print("My tool output")
   ```

2. Add an entry point in `pyproject.toml`:

   ```toml
   [project.scripts]
   my-tool = "my_tool:main"
   ```

3. Create tests in `src/tests/`:

   ```python
   # src/tests/test_my_tool.py
   from my_tool import main

   def test_my_tool():
       # Your test here
       pass
   ```

4. Test your tool:

   ```bash
   # Run locally
   uv run my-tool

   # Test with uvx
   uvx --from . my-tool
   ```

### Running Tests

```bash
# Run all tests
uv run pytest

# Run specific test file
uv run pytest src/tests/test_hello.py

# Run with verbose output
uv run pytest src/tests/ -v

# Run with coverage
uv run pytest src/tests/ --cov=hello
```

### Code Quality

Before committing, ensure your code meets quality standards:

```bash
# Format code (if ruff is added)
uv run ruff format .

# Lint code (if ruff is added)
uv run ruff check .

# Type check (if mypy is added)
uv run mypy src/
```

## Using the Tools

### With uv run (local development)

```bash
uv run hello
uv run hello "Your Name"
```

### With uvx (anywhere)

```bash
# From local directory
uvx --from . hello

# From GitHub with SSH
uvx --from git+ssh://git@github.com/carpusherw/tool-python-dev.git hello
```

## For Coding Agents

### Key Information

- **Package Manager**: uv
- **Python Version**: 3.14+
- **Test Framework**: pytest
- **Project Type**: Application/CLI tools

### Common Tasks

1. **Add a dependency**:

   ```bash
   uv add <package-name>
   ```

2. **Add a dev dependency**:

   ```bash
   uv add --dev <package-name>
   ```

3. **Run commands in the virtual environment**:

   ```bash
   uv run <command>
   ```

4. **Install the project in editable mode**:

   ```bash
   uv sync
   ```

### Testing Changes

Always test changes before committing:

```bash
# Run tests
uv run pytest -v

# Test the CLI tool
uv run hello
uvx --from . hello
```

### Code Style

- Use type hints whenever possible
- Write docstrings for modules, classes, and functions
- Keep functions small and focused
- Write tests for new functionality
- Follow PEP 8 style guidelines

## Troubleshooting

### Common Issues

**Issue**: `uv: command not found`

- **Solution**: Install uv following the instructions in Prerequisites section

**Issue**: `ModuleNotFoundError` when running tests

- **Solution**: Run `uv sync` to ensure all dependencies are installed

**Issue**: Changes not reflected when running tool

- **Solution**: The package is installed in editable mode, but you may need to restart your terminal or run `uv sync` again

## Getting Help

- Check the [uv documentation](https://docs.astral.sh/uv/)
- Open an issue in the repository
- Review existing tests and tools for examples
