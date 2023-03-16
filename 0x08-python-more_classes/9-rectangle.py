#!/usr/bin/python3
""" Class that defines a Rectangle """


class Rectangle:

    """ Public class attribute """
    number_of_instances = 0
    print_symbol = "#"

    """ Init Method """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    """ Area Method """
    def area(self):
        return self.width * self.height

    """ Perimeter Method """
    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    """ Str Method """
    def __str__(self):
        rectangle = ""
        if self.__width == 0 or self.__height == 0:
            return rectangle
        for column in range(self.__height):
            for row in range(self.width):
                rectangle += str(self.print_symbol)
            if column != self.__height - 1:
                rectangle += "\n"
        return rectangle

    """ Repr Method """
    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

    """ Del Method """
    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    """ Static method """
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not type(rect_1) == Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not type(rect_2) == Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")

        rec1 = rect_1.width + rect_1.height
        rec2 = rect_2.width + rect_2.height

        if rec1 == rec2:
            return rect_1
        elif rec1 > rec2:
            return rect_1
        else:
            return rect_2

    """ class method """
    @classmethod
    def square(cls, size=0):
        new_instance = Rectangle(size, size)
        return new_instance
