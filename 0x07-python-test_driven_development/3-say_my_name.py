#!/usr/bin/python3
"""
Module for say_my_name
"""


def say_my_name(first_name, last_name=""):
    """
    Print Full Nname for a person.
    """
    if type(first_name) != str:
        raise TypeError('First_name must be a string')
    if type(last_name) != str:
        raise TypeError('Last_name must be a string')
    print("My name is {:s} {:s}".format(first_name, last_name))

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")
