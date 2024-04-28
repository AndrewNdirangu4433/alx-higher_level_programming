#!/usr/bin/python3
"""
This is a module with a function to add two integers
"""


def add_integer(a, b=98):
    """
    This is a function to add two integers

    Agrs:
    a: is a given integer or float
    b: is a given integer or float

    Return:
    The sum of a and b

    Raises:
    TypeError: raise TypeError if a or b is not an integer or float
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    if isinstance(a, int) and isinstance(b, int):
        return int(a) + int(b)
    if isinstance(a, int) and isinstance(b, float):
        return int(a) + int(b)
    if isinstance(a, float) and isinstance(b, float):
        return int(a) + int(b)
    if isinstance(a, float) and isinstance(b, int):
        return int(a) + int(b)
