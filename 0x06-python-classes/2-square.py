#!/usr/bin/python3
"""square module."""


class Square:
    """Define a square"""

    def __init__(self, size):
        """Initialize the data.

        Args:
            size: length of a size of the square.

        Raises:
            TypeError : if size not an integer
            ValueErorr: if size is less than 0
        """

        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
