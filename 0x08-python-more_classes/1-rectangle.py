#!/usr/bin/Python3
""" Class that defines a Rectangle """


class Rectangle:

    """ Init Method """
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    """ property and setter for width """
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    """ property and setter for height """
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
