#!/usr/bin/python3
"""
This is a module with function that prints a text with 2 new lines,
after each of these characters: ., ? and :
"""


import re

def text_indentation(text):
    """
    This is a function that prints a text with 2 new lines,
    after each of these characters: . , ? and :

    Args:
    text: this is a text passed into the function.

    Returns:
    Indedntation with 2 new lines at each specified symbol.

    Raises:
    TypeError: raise a TypeError if text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for delimeter in "?:.":
        print((delimeter + "\n\n"))

