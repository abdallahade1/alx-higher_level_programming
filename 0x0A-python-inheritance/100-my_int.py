#!/usr/bin/python3
"""Module12"""


class MyInt(int):
    """MyInt class"""

    def __eq__(self, other):
        """method for inverting =="""
        return self.real != other

    def __ne__(self, other):
        """Method for inverting !="""
        return self.real == other
