#!/usr/bin/python3
"""
Module reconstruct a json data into its origin
"""
from json import loads


def from_json_string(my_str):
    """
    Function to returns an object (Python data structure)
    represented by a JSON string

    Args:
    my_str (str): data to be converted

    Returns:
    The converted data
    """
    return loads(my_str)
