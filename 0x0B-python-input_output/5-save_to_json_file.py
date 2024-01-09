#!/usr/bin/python3
"""
Module to writes an Object to a text file, using a JSON representation
"""
from json import dumps


def save_to_json_file(my_obj, filename):
    """
    Function to writes an Object to a text file, using a JSON representation

    Args:
    my_obj: object to be written
    filename (str): name of the file
    """
    with open(filename, 'w') as f:
        f.write(dumps(my_obj))
