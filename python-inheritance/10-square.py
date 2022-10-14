#!/usr/bin/python3
""" Module that contains a class Square """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Class Square """

    """ Init Method """

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    """ Area Method """

    def area(self):
        return self.__size * self.__size
