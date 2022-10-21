#!/usr/bin/python3
""" Module with a class Base """
import json


class Base:
    """ Class Base """

    __nb_objects = 0

    """ Constructor """

    def __init__(self, id=None):
        self.id = id

        if self.id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Dictionary to JSON string """

        if list_dictionaries is None or len(list_dictionaries) <= 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
