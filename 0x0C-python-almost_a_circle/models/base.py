#!/usr/bin/python3
"""Model 1"""
import json


class Base:
    """the base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """class representation"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """JSON representation"""
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes Json representation"""
        if list_objs is not None:
            list_objs = [o.to_dictionary() for o in list_objs]
        with open("{}.json".format(cls.__name__), "w",
                  encoding="utf-8") as file:
            file.write(cls.to_json_string(list_objs))
