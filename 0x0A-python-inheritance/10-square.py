#!/usr/bin/python3
"""Module10"""
Rectangle = __import__("9-rectangle.py").Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size):
        """initializing a square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """area of a square"""
        return self.__size ** 2
