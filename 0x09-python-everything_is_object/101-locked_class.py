#!/usr/bin/python3
"""
defines a locked class
"""


class LockedClass:
    """
    Prevents the user from dynamically creating new instance attributes,
    except if the new instance is 'first_name'
    """

    __slots__ = ["first_name"]
