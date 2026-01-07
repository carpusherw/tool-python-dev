"""Unit tests for the hello tool."""

import pytest
from tool_python_dev.hello import greet


def test_greet_default():
    """Test greet with no name provided."""
    result = greet()
    assert result == "Hello, World!"


def test_greet_with_name():
    """Test greet with a name provided."""
    result = greet("Alice")
    assert result == "Hello, Alice!"


def test_greet_with_empty_string():
    """Test greet with an empty string."""
    result = greet("")
    assert result == "Hello, World!"


def test_greet_with_multiple_words():
    """Test greet with a name containing multiple words."""
    result = greet("Alice Smith")
    assert result == "Hello, Alice Smith!"
