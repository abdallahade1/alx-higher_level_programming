#!/usr/bin/python3
"""
function to add two numbers
"""


def add_integer(a, b=98):
    """
    This function returns
    the sum of two numbers
    """

    if type(a) != int and type(b) != float:
        raise TypeError("a must be an integer")
    if type(b) != int and type(a) != float:
        raise TypeError("b must be a float")
    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)
    return a + b
