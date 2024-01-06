#!/usr/bin/python3
"""
This module contains function add that adds two integers
"""


def add_integer(a, b=98):
    """
    This function is adding two integers

    Parameters:
    - a: the first number
    - b: the second number

    Returns:
    - int: the result of the addition process
    """
    if a is None:
        raise TypeError("missing one argument")
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if isinstance(a, float):
        a = int(a)
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    if isinstance(b, float):
        b = int(b)
    return a + b
