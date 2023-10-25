#!/usr/bin/python3
"""Define a class square"""


class Square:
    """Defines a square

    Attributes:
        size: size of a square (1 side).
    """
    def __init__(self, size=0):
        """Initialises the data

         Args:
            size: size of the square (1 side).
        """
        self.size = size

    def area(self):
        """Calculates the area

        Returns: current square area
        """
        return self.__size**2

    @property
    def size(self):
        """
        Retuens the size of the square
        """

        return self.__size

    @size.setter
    def size(self, value):
        """Property setter for size.

        Args:
            value (int): size of a square (1 side).

        Raises:
            TypeError: size must be an integer
            ValueError: size must be >= 0
        """
        self.__size = value
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
