#!/usr/bin/python3
""" class Square that defines a square """


class Square:
    """ Private instance attribute: size
        size must be an integer
        size must be greater than 0 """
    def __init__(self, size):
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    """ Public instance method that returns the current square area"""
    def area(self):
        area = self.__size ** 2
        return area
