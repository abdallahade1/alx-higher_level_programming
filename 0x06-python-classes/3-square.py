#!/usr/bin/python3
"""define a class a square."""


class Square:
    """Defines a square

    Attributes:
        size: size of the square
    """
    def __init__(self, size=0):
        """Initialises the data

        Args:
            size: size of the square (1 side).
        """
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Calculate the area

        Returns: current square area.
        """
        return self.__size ** 2
