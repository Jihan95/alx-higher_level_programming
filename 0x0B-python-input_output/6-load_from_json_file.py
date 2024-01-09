#!/usr/bin/python3
"""
Module to creates an Object from a “JSON file”
"""
from json import loads


def load_from_json_file(filename):
    """
    Function to creates an object from JSON File

    Args:
    filename (str): the file name
    """
    with open(filename) as f:
        return loads(f.read())
