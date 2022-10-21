#!/usr/bin/python3
"""
Module that contains the class saquare
tha inherits from Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class Square that inherits from Rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        """ Constructor method """

        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Str method """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.__width}"

    @property
    def size(self):
        """ Getter """

        return self.__width

    @size.setter
    def size(self, value):
        """ Setter """

        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        self.__height = value
