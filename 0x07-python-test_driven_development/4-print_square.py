#!/usr/bin/python3
"""
This is a module to print symbol "#" into a square of given length (size)
"""


def print_square(size):
    """
    This is a function to print "#" as specified by size.

    Args:
    size: is a given integer that dictates the length of the printed symbol(#)

    Returns:
    print out of the symbol"#" into square shapes of specified lengths

    Raises:
    TypeError: raise TypeError if size is not an integer
    ValueError: raise ValueError if size is less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if isinstance(size, int):
        if size < 0:
            raise ValueError("size must be >= 0")
        if size >= 0:
            for i in range(size):
                print("#"*size)
