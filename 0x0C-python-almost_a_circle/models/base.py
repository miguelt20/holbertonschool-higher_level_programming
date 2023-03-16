#!/usr/bin/python3
""" Module with a class Base """
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Dictionary to JSON string """

        if list_dictionaries is None or len(list_dictionaries) <= 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ JSON string to file """

        filename = cls.__name__ + ".json"
        obj_list = []
        if list_objs is not None:
            for o in list_objs:
                obj_list.append(cls.to_dictionary(o))
        with open(filename, 'w') as f:
            f.write(cls.to_json_string(obj_list))

    @staticmethod
    def from_json_string(json_string):
        """ JSON string to dictionary """

        if json_string is None or len(json_string) <= 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Dictionary to Instance """

        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy = cls(1)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ File to instances """

        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as f:
                list_dicts = Base.from_json_string(f.read())
                return [cls.create(**elem) for elem in list_dicts]
        except IOError:
            return []
