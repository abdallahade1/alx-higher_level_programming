#!/usr/bin/python3
"""Module13"""


def add_attribute(obj, name, value):
    """Method for adding attribute"""

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, name, value)
