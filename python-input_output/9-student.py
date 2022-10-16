#!/usr/bin/python3
"""
Module that contains a class Student
that defines a student by some attributes.
"""


class Student:
    """ Student class """

    """ Constructor """

    def __init__(self, first_name, last_name, age):
        self.f_name = first_name
        self.l_name = last_name
        self.age = age

    """ Json Method """

    def to_json(self):
        return self.__dict__
