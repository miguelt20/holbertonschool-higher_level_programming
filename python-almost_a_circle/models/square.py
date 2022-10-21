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

    def update(self, *args, **kwargs):
        """ Assigns an argument to each attribute
            using args or kwargs.
            Updating the Rectangle """

        if args is not None and len(args) != 0:
            self.id = args[0]
            if len(args) > 1:
                self.__width = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.__width = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """ Dictionary representation """

        dict_rep = {
            "id": self.id,
            "size": self.__width,
            "x": self.x,
            "y": self.y
        }

        return dict_rep
