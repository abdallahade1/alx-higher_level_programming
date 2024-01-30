#!/usr/bin/python3
"""Function that finds a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """Returns peak of list_of_intergers"""
    if list_of_integers == []:
        return None

    list_int = len(list_of_integers)
    if list_int == 1:
        return list_of_integers[0]
    elif list_int == 2:
        return max(list_of_integers)

    mid = int(list_int / 2)
    peak = list_of_integers[mid]
    if peak > list_of_integers[mid - 1] and peak > list_of_integers[mid + 1]:
        return peak
    elif peak < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
    else:
        return find_peak(list_of_integers[mid + 1:])
