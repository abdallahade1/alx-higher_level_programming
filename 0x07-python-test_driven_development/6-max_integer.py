#!/usr/bin/python3
"""Module for max_integer
"""


def max_integer(list=[]):
    """
    This function to find and return the max integer in a list and
    If the list is empty, the function returns None
    """
    if len(list) == 0:
        return None
    new_list = list[0]
    i = 1
    while i < len(list):
        if list[i] > new_list:
            new_list = list[i]
        i += 1
    return new_list
