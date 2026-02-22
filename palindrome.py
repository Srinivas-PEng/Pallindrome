"""
Validates strings as palindromes.
Assignment #4
Srinivas Ganapathyraju
"""
from collections import deque

def is_palindrome(value: str) -> bool:
    if not isinstance(value, str):
        raise ValueError("Input must be a string")

    if value == "":
        return False

    chars = deque(value)
    while len(chars) >1:
        if chars.popleft() !=chars.pop():
            return False

    return True
