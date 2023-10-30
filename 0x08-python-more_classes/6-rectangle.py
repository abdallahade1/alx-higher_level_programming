#!/usr/bin/python3

"""
This is a module for a class Rectangle
"""


class Rectangle:
    """Class of a Rectangle"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize class"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Get width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate area"""
        return self.__width * self.__height

    def perimeter(self):
        """Calculate perimeter"""
        width = self.__width
        height = self.__height
        if width == 0 or height == 0:
            return 0
        return (width + height) * 2

    def __str__(self):
        """Get string representation"""
        width = self.__width
        height = self.__height
        string = ""
        if width == 0 or height == 0:
            return string
        for i in range(height):
            for y in range(width):
                string = string + '#'
            string = string + '\n'
        return string[:-1]

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances += 1
