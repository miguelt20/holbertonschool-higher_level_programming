#!/usr/bin/python3
"""
This module contains a function that divides
all elements of a matrix and returns a new matrix
with elements with the result of the division
"""


def matrix_divided(matrix, div):
    """
    Function that divides all elements of a matrix
    """
    if not len(set(map(len, matrix))) == 1:
        raise TypeError("Each row of the matrix must have the same size")
    if div == float('inf'):
        raise OverflowError("cannot convert float to integer")
    if not isinstance(div, int or float or float('inf') or float('-inf')):
        raise TypeError("div must be a number")
    for row in matrix:
        for element in row:
            if element == 0:
                raise ZeroDivisionError("division by zero")
            if isinstance(element, int) or isinstance(element, float):
                continue
            else:
                raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")
    new_matrix = [[round(element/div, 2) for element in row]for row in matrix]
    return new_matrix
