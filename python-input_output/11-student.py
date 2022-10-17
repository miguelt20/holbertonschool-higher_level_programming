#!/usr/bin/python3
"""
Module that contains a class Student
that defines a student by some attributes.
"""


class Student:
    """ Student class """

    """ Constructor """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    """ Json Method """

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        my_dict = {}
        for at in attrs:
            try:
                my_dict[at] = self.__dict__[at]
            except KeyError:
                pass
        return my_dict

    """ Function that replces attributes of the student instance """

    def reload_from_json(self, json):

        for key, value in json.items():
            self.__dict__[key] = value
