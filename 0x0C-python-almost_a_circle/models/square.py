#!/usr/bin/python3
"""Module 10"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializing the class"""
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """Str representaion"""
        return '[Square] ({}) {}/{} - {}'.\
            format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """retrieve size"""
        return self.width

    @size.setter
    def size(self, value):
        """set width and height with the same value, value"""
        self.width = value
        self.height = value
