#!/usr/bin/python3
""" class Square that defines a square """


class Square:
    """ Private instance attribute """

    """ Init Method """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    """ property """
    @property
    def size(self):
        return self.__size

    """ size etter """
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    """ property """
    @property
    def position(self):
        return self.__position

    """ setter position """
    @position.setter
    def position(self, value):
        mssg = 'position must be a tuple of 2 positive integers'
        if not isinstance(value, tuple):
            raise TypeError(mssg)
        if len(value) != 2:
            raise TypeError(mssg)
        if not isinstance(value[0], int):
            raise TypeError(mssg)
        if not isinstance(value[1], int):
            raise TypeError(mssg)
        if value[0] < 0 or value[1] < 0:
            raise TypeError(mssg)
        self.__position = value

    """ Method to get square area"""
    def area(self):
        if self.__size == 0:
            return 0
        else:
            area = self.__size ** 2
        return area

    """ Method that prints the square """
    def my_print(self):
        if self.size == 0:
            print()
        else:
            for i in range(self.position[1]):
                print()
            for i in range(0, self.size):
                for k in range(self.position[0]):
                    print(" ", end='')
                for j in range(self.size):
                    print("#", end='')
                print()
