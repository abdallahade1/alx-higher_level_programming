#!/usr/bin/python3

"""
Module for text_indentation
"""

def text_indentation(text):

    """
    prints the text
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    itr = 0
    for i in text:
        if i == '?' or i == ':' or i == '.':
            print(i, end="\n\n")
            itr = 1
        else:
            if itr == 0:
                print(i, end="")
            else:
                if i == ' ' or i == '\t':
                    pass
                else:
                    print(i, end="")
                    itr = 0
