#!/usr/bin/python3
"""Module4"""


def inherits_from(obj, a_class):
    """Returns:
    True: if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class
    False: Otherwise
    """
    return isinstance(obj, a_class) and type(obj) != a_class
