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
    counter = 0
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for char in text:
        if text[counter - 1] == '.' or\
         text[counter - 1] == '?' or text[counter - 1] == ':':
            char = ""
            print("\n")
        print(char, end="")
        counter += 1
