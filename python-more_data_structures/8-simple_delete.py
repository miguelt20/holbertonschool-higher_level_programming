#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    for keys in a_dictionary:
        if a_dictionary is None:
            return None
        else:
            rm = a_dictionary.pop(key, None)
            if rm is None:
                return a_dictionary
            else:
                return a_dictionary
