#!/usr/bin/python3
"""Module to find the max integer in a list
"""


def max_integer(my_list=[]):
    """Function to find and return the max integer in a list of integers
        If the list is empty, the function returns None
    """
    if my_list is None:
        return None
    if not isinstance(my_list, list):
        raise TypeError("passsed value should be a list")
    result = my_list[0]
    for num in my_list:
        if not isinstance(num, int):
            raise ValueError("passed value should be a list of integers")
        if num > result:
            result = num
    return result
