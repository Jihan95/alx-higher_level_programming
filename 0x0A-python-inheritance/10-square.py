#!/usr/bin/python3
"""
Module that contain an BaseGeometry class
and a recatangle class
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class that represents a square

    Attributes:
    __size (int): the length of the square
    """
    def __init__(self, size):
        """
        Function that intantiate a square object
        """
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Function to return the area of the square
        """
        return self.__size ** 2
