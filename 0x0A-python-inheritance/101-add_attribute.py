#!/usr/bin/python3
"""
Module to add attribute
"""


def add_attribute(obj, name, value):
    """
    Function that add attribute
    """
    if not isinstance(name, str) or value is None:
        raise TypeError("can't add new attribute")
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
