#!/usr/bin/python3
"""
Module 12-pascal_triangle
"""


def pascal_triangle(n):
    """
    represents the pascal's triangle of size n
    Return: a list of lists of integers representing the triangle
    """
    if n <= 0:
        return []
    if n == 1:
        return [[1]]

    triangle = [[1]]
    for rows in range(n-1):
        triangle.append([a+b for a, b
                         in zip([0] + triangle[-1], triangle[-1] + [0])])
    return triangle
