#!/usr/bin/python3
"""
Module that contain Mylis class
"""


class MyList(list):
    """
    A class representing a list
    """
    def print_sorted(self):
        """
        function to prints the list, but sorted (ascending sort)
        """
        for value in self:
            if not isinstance(value, int):
                raise ValueError("list must be a list of integers")
        print(sorted(self))
