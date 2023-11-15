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

    def from_json_string(json_string):
        """Returns The list of json representaion"""
        if json_string is None or json_string == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns all instances of anything set"""
        from models.rectangle import Rectangle
        from models.square import Square
        if cls is Rectangle:
            new_instance = Rectangle(3, 4)
        elif cls is Square:
            new_instance = Square(5)
        else:
            new_instance = None
        new_instance.update(**dictionary)
        return new_instance
