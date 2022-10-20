#!/usr/bin/python3
""" Module with a class Base """


class Base:
    """ Class Base """

    __nb_objects = 0

    """ Constructor """

    def __init__(self, id=None):
        self.id = id

        if self.id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
