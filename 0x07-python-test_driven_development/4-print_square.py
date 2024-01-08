#!/usr/bin/python3
"""
This module contains function that prints a square
"""


def print_square(size):
    """
    This function prints a square

    Parameters:
    -size (int): the length of square
    """
    if size is None:
        raise TypeError("print_square() missing 1 required positional argument: 'size'")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print('#' * size)
