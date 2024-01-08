#!/usr/bin/python3
"""
Module contains a function to check an object
"""


def inherits_from(obj, a_class):
    """
    Function that checks if an object is an is an instance of a class
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
