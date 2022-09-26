#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    for keys in a_dictionary:
        rm = a_dictionary.pop(key, None)
        if len(a_dictionary) == 0:
            return
        elif rm is None:
            return a_dictionary
        else:
            return a_dictionary
