#!/usr/bin/python3
"""
Module that contain rebel class
"""


class MyInt(int):
    """
    A rebel in class
    """
    def __eq__(self, other):
        """
        Override the == operator to behave as !=
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Override the != operator to behave as ==
        """
        return super().__eq__(other)
