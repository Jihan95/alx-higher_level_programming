#!/usr/bin/python3
"""
This module contains say_my_name function
"""


def say_my_name(first_name, last_name=""):
    """
    prints a name

    Parameters:
    - first_name (string): the first name
    - last_name (string): the last name
    """
    if first_name is None:
        raise TypeError("say_my_name() missing 1 required positional"
                        " argument: 'first_name'")
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
