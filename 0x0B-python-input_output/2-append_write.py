#!/usr/bin/python3
"""
Module to appends data to text file
"""


def append_write(filename="", text=""):
    """
    Function to append data to a text file

    Args:
    filename (str): the file name
    text (str): text to be appended

    Returns: returns the number of characters added
    """
    with open(filename, 'a') as f:
        return f.write(text)
