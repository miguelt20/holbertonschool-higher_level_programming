#!/usr/bin/python3
"""
Module that contains a function
that appends a string at the end of a text file
and returns the number of characters added
"""


def append_write(filename="", text=""):
    """ Function that appends a string """

    with open(filename, 'a', encoding="utf-8") as f:
        chars_added = f.write(text)

        return chars_added
