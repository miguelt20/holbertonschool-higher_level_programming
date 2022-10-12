#!/usr/bin/python3
""" 
Module that contains a function
returns the list of available
attributes and methods of an object.
"""


def lookup(obj):
    """ Funciton that returns the list """
    list_obj = dir(obj)
    return list_obj
