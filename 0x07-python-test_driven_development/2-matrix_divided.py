#!/usr/bin/python3
"""
This is a module with a function to divide elements in the lists of a matrix
"""


def matrix_divided(matrix, div):
    """
    This is a function that divides all elements of a matrix.

    Args:
    matrix: this is a matrix
    div: an integer to divide the elements by

    Returns:
    a new matrix from the reslting divisions

    Raises:
    TypeError: raise a TypeError if div is not a number
               raise a TypeError if matrix is not a list of lists(integers/floats)
               raise a TypeError if each row of the matrix is not the same size
    ZeroDivisionError: raise ZeroDivisionError if div is 0
    """
    errMsg = "matrix must be a matrix (list of lists) of integers/floats"
    if not matrix:
        raise TypeError(errMsg)
    if not isinstance(matrix, list):
        raise TypeError(errMsg)
    for lists in matrix:
        if not isinstance(lists, list):
            raise TypeError(errMsg)
        for item in lists:
            if not isinstance(item, int) and not isinstance(item, float):
                raise TypeError(errMsg)
    for lists in matrix:
        if len(lists) == 0:
            raise TypeError(errMsg)
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if not all(len(lists) == len(matrix[0]) for lists in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(item / div, 2) for item in lists] for lists in matrix]

