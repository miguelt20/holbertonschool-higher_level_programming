#!/usr/bin/python3
"""
Module that contains a function
that verifies if an object is an instance of a class that
inherited (directly or indirectly) from the specified class.
"""


def inherits_from(obj, a_class):
    """ Function that verifies """

    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    else:
        return False
