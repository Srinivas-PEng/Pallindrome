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

    normalized = "".join(
        char.lower() for char in value if char !=""
    )

    chars = deque(normalized)
    while len(chars) >1:
        if chars.popleft() !=chars.pop():
            return False

    return True
