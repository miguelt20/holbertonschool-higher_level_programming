#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    for keys in a_dictionary:
        rm = a_dictionary.pop(key, None)
        if a_dictionary is None:
            return a_dictionary
        elif rm is None:
            return a_dictionary
        else:
            return a_dictionary
