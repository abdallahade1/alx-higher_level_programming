#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx  >= len(my_list):
        return my_list
    list_copy = my_list.copy()
    list_copy = list_copy.remove(idx)
    return list_copy
