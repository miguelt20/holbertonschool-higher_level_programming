#!/usr/bin/python3
"""
This module contains a function that add
two integers and returns the result of the
addition.
"""


def add_integer(a, b=98):
    """
    Function that adds two integers
    """
    try:
        if isinstance(a, float):
            a = int(a)
        elif isinstance(b, float):
            b = int(b)
        res = a + b
    except TypeError:
        if not isinstance(a, int):
            raise TypeError("a must be an integer")
        elif not isinstance(b, int):
            raise TypeError("b must be an integer")
    return res
