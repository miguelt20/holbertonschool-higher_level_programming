#!/usr/bin/python3
"""
Module that contains a function
that checks if an object is exactly
an instance of the specified class
"""


def is_same_class(obj, a_class):
    """ Function that verifies """
    if type(obj) is a_class:
        return True
    else:
        return False
