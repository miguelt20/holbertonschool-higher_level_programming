#!/usr/bin/python3
"""
Module that contains a function
that writes a string in a text file
and returns the number of characters
"""


def write_file(filename="", text=""):
    """ Function that writes a string """

    with open(filename, 'w', encoding="utf-8") as f:
        chars = f.write(text)
    return chars
