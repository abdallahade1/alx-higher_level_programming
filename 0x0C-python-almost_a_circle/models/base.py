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
