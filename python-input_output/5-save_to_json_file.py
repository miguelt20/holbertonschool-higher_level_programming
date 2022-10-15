#!/usr/bin/python3
"""
Module that contains a function
that writes an Object to a text file,
using a JSON representation.
"""
import json


def save_to_json_file(my_obj, filename):
    """ Function that writes an Object to a text file with JSON """
    json_format = json.dumps(my_obj)
    with open(filename, "w", encoding="utf-8") as f:
        f.write(json_format)
