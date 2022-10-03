#!/usr/bin/python3
""" class Square that defines a square """


class Square:
    """ Private instance attribute """

    """ Init Method """
    def __init__(self, size=0):
        self.__size = size

    """ property """
    @property
    def size(self):
        return self.__size

    """ Setter """
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    """ Method to get square area"""
    def area(self):
        if self.__size == 0:
            return 0
        else:
            area = self.__size ** 2
        return area
