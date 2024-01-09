#!/usr/bin/python3
"""
module to write a string into a file
"""


def write_file(filename="", text=""):
    """
    Function to write a string in a file

    Args:
    filename (str): the name of the file
    text (str): text to be written

    Returns:
    the number of characters written
    """
    with open(filename, 'w') as f:
        return f.write(text)
