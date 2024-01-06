#!/usr/bin/python3
"""
This module contains function for test indentation
"""


def text_indentation(text):
    """
    This function that prints a text with 2 new lines
    after each of these characters: ., ? and :

    Parameters:
    - text (str): the text to be printed
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    flag = 0
    for alpha in text:
        if flag == 1:
            print("\n")
        if alpha in ['.', '?', ':']:
            print(alpha, end='')
            flag = 1
        elif alpha == ' ' and flag == 1:
            flag = 0
        else:
            print(alpha, end='')
            flag = 0
    if flag == 1:
        print("\n")
