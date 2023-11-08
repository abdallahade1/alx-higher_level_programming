#!/usr/bin/python3
"""Model8"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry



class Rectangle(BaseGeometry):
    """class rectangle inherits from
    7-base_geometry"""

    def __init__(self, width, height):
        """initializing the method"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
