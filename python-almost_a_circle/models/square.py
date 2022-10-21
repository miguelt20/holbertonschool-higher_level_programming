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
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """ Str method """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
