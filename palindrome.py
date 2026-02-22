"""
Validates strings as palindromes.
Assignment #4
Srinivas Ganapathyraju
"""
def is_palindrome(value: str) -> bool:
    if not isinstance(value, str):
        raise ValueError("Input must be a string")