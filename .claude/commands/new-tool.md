# New Tool

Add a new CLI tool to the project following established patterns.

## Action Description

$ARGUMENTS

Examples:

- `/new-tool sign_jwt` - Create a tool named sign_jwt
- `/new-tool` - Will ask for tool details interactively

## Required Information

Make sure the following information is acquired before proceeding:

1. **Tool name** (snake_case, e.g., `sign_jwt`)
2. **Arguments** - Positional and optional arguments the tool accepts
3. **What does the tool do?** - Brief description of the tool's purpose

## Files to Modify

1. `src/<tool_name>.py` - Create the tool module
2. `pyproject.toml` - Add entry point under `[project.scripts]`
3. `src/tests/test_<tool_name>.py` - Create unit tests
4. `README.md` - Add to Available Tools list and document usage
5. `AGENTS.md` - Update project structure and tool testing instructions

## Steps

1. **Create the tool module** in `src/<tool_name>.py`:
   - Include a main function as the entry point
   - Reference `src/hello.py` for simple tools or `src/sign_jwt.py` for tools with arguments

2. **Add entry point** in `pyproject.toml`:
   - Add under `[project.scripts]` section using snake_case
   - Example: `tool_name = "tool_name:main"`

3. **Create tests** in `src/tests/test_<tool_name>.py`:
   - Write unit tests for the tool's functionality
   - Reference `src/tests/test_hello.py` or `src/tests/test_sign_jwt.py` as examples

4. **Add dependencies** if needed:
   - Use `uv add <package>` for runtime dependencies
   - Use `uv add --dev <package>` for dev dependencies

5. **Update documentation**:
   - Add tool to the list in `README.md` under "## Available Tools"
   - Add a new section with usage, arguments, options, and examples
   - Update `AGENTS.md` for project structure and tool testing instructions
     - Check if other sections need to be updated
   - Check if this command (new-tool) needs to be updated

6. **Verify**:
   - Run `uv sync` to install dependencies
   - Run `uv run pytest -v` to ensure all tests pass
   - Test the CLI with `uv run <tool_name> --help`
   - Test with uvx using `uvx --from . <tool_name> --help`
   - Test the tool. Ask if you don't know the parameters to use.
