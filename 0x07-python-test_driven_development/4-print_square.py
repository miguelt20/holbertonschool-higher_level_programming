#!/usr/bin/python3
"""
Module that contains a function
that prints a square with the
character "#".
"""


def print_square(size):
    """
    Function that prints a square.
    """
    if not isinstance(size, int) or isinstance(size, float):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
