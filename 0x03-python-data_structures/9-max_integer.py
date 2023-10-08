#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    list_sort = my_list.copy()
    list_sort = list_sort.sort()
    print("{:d}".format(list_sort[-1]))
