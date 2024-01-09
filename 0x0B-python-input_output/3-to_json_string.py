#!/usr/bin/python3
"""
Module to returns JSON representation of an object
"""
from json import dumps


def to_json_string(my_obj):
    """
    Function to convert an object to its JSON representation

    Args:
    my_obj: object to be converted

    Returns:
    The JSON representation of my_obj
    """
    return dumps(my_obj)
