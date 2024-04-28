#!/usr/bin/python3
"""
This is a module that prints a message "My name is <first_name> <last_name>"
"""


def say_my_name(first_name, last_name=""):
    """
    This is a function to print "My name is <first name> <last name>"

    Args:
    first_name: is a string argument passed as the first name
    last_name: is a string argument passed as the last name

    Returns:
    The message "My name is <first name> <last name>" with the necessary args

    Raises:
    TypeError: raise TypeError if first_name or last_name is not a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    if isinstance(first_name, str):
        print("My name is {} {}".format(first_name, last_name))
