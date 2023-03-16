#!/usr/bin/python3
""" Module that contains a class Rectangle """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Class Rectangle """

    """ Init Method """

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    """ Area Method """

    def area(self):
        return self.__width * self.__height

    """ Str Method """

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"
