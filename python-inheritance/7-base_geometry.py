#!/usr/bin/python3
""" Module that contains a class BaseGeometry """


class BaseGeometry:
    """ class BaseGeometry """

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        self.name = name
        self.value = value
        if type(value) != int:
            raise TypeError(f"{self.name} must be an integer")
        if value <= 0:
            raise ValueError(f"{self.name} must be greater than 0")
