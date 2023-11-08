#!/usr/bin/python3
"""Module3"""


def is_kind_of_class(obj, a_class):
    """Returns:
    True: if the object is an instance of, or 
    if the object is an instance of a class that inherited from.
    False: Otherwise
    """
    return isinstance(obj, a_class)
