"""
Tests the palindrome module
Assignment #4
Srinivas Ganapathyraju
"""
import pytest
from palindrome import is_palindrome

def test_raises_value_error_when_not_string():
    with pytest.raises(ValueError):
        is_palindrome(123)

def test_empty_string_returns_false():
    assert is_palindrome("") is False

def test_single_character_returns_true():
    assert is_palindrome("a") is True