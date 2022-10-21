#!/usr/bin/python3
""" Module with a class """
from models.base import Base


class Rectangle(Base):
    """ Class Rectangle inherits from Base """

    """ Constructor """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    """ Getters and Setters """
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Area method """

        return self.__width * self.__height

    def display(self):
        """ Displays method that prints a rectangle """

        for i in range(self.__y):
            print()
        for j in range(self.__height):
            for k in range(1):
                print(" " * self.__x, end="")
                print("#" * self.__width, end="")
            print()

    def __str__(self):
        return f"[Rectangle] ({self.id}) {self.__x}/\
{self.__y} - {self.__width}/{self.__height}"
