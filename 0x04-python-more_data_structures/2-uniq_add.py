#!/usr/bin/python3
def uniq_add(my_list=[]):
    list_uniq = set(my_list)
    j = 0
    for i in list_uniq:
        j += i
    return j
