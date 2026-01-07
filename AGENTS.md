# Contributing to tool-python-dev

This guide explains how to work with this repository, whether you're a human developer or a coding agent.

## Project Overview

This is a uv-based Python project that provides helper tools for development teams. The tools can be run using `uvx` without requiring installation.

## Prerequisites

- Python 3.12 or higher
- [uv](https://github.com/astral-sh/uv) - Fast Python package installer and resolver

### Installing uv

```bash
# On macOS and Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Using pip
pip install uv

# Using pipx
pipx install uv
```

## Getting Started

### Clone and Setup

```bash
# Clone the repository
git clone https://github.com/carpusherw/tool-python-dev.git
cd tool-python-dev

# Install dependencies
uv sync

# Run tests
uv run pytest tests/
```

### Project Structure

```
tool-python-dev/
├── src/
│   └── tool_python_dev/
│       ├── __init__.py
│       └── hello.py          # Hello world helper tool
├── tests/
│   └── test_hello.py         # Unit tests
├── pyproject.toml            # Project configuration
├── README.md                 # User documentation
├── AGENTS.md                 # This file
└── CLAUDE.md                 # Symlink to AGENTS.md
```

## Development Workflow

### Adding a New Tool

1. Create a new module in `src/tool_python_dev/`:
   ```python
   # src/tool_python_dev/my_tool.py
   def main() -> None:
       """Main entry point for the tool."""
       print("My tool output")
   ```

2. Add an entry point in `pyproject.toml`:
   ```toml
   [project.scripts]
   my-tool = "tool_python_dev.my_tool:main"
   ```

3. Create tests in `tests/`:
   ```python
   # tests/test_my_tool.py
   from tool_python_dev.my_tool import main
   
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
uv run pytest tests/

# Run specific test file
uv run pytest tests/test_hello.py

# Run with verbose output
uv run pytest tests/ -v

# Run with coverage
uv run pytest tests/ --cov=tool_python_dev
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

# From published package (when published to PyPI)
uvx tool-python-dev hello
```

## Building and Publishing

### Build the package

```bash
# Build wheel and source distribution
uv build
```

### Publish to PyPI (when ready)

```bash
# Test on TestPyPI first
uv publish --repository testpypi

# Publish to PyPI
uv publish
```

## For Coding Agents

### Key Information

- **Package Manager**: uv (not pip, poetry, or pipenv)
- **Python Version**: 3.12+
- **Test Framework**: pytest
- **Project Type**: Application/CLI tools (not a library)

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
uv run pytest tests/ -v

# Test the CLI tool
uv run hello
uvx --from . hello
```

### Code Style

- Use type hints for function parameters and return values
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

## License

This project is open source. Please check the LICENSE file for details.
