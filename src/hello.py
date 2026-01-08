"""A simple hello-world helper tool."""

import sys
from typing import Optional


def greet(name: Optional[str] = None) -> str:
    """
    Generate a greeting message.

    Args:
        name: Optional name to greet. If not provided or empty, uses "World".

    Returns:
        A greeting message string.
    """
    if name and name.strip():
        return f"Hello, {name}!"
    return "Hello, World!"


def main() -> None:
    """Main entry point for the hello tool."""
    name = None
    if len(sys.argv) > 1:
        name = sys.argv[1]

    message = greet(name)
    print(message)


if __name__ == "__main__":
    main()
