#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    elements = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            elements.append(True)
        else:
            elements.append(False)

    return (elements)
