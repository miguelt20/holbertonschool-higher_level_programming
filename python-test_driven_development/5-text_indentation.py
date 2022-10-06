#!/usr/bin/python3
"""
Module that contains a functions
that prints a text with 2 new lines
after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    Function that prints a text
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new_line = False
    for char in text:
        if new_line:
            if char == " ":
                continue
            new_line = False
        if char == '.' or char == '?' or char == ':':
            print(char)
            print()
            new_line = True
        else:
            print(char, end="")
