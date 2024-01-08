#!/usr/bin/python3
"""
Module to look an object up
"""


def lookup(obj):
    """
    Function to  list of available attributes and methods of an object

    Args
    obj : the object to lookup

    Returns:
    a list of its available attributes and methods
    """
    return list(dir(obj))
