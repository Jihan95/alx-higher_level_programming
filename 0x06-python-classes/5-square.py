#!/usr/bin/python3
"""This module contains a class definition for representing squares."""


class Square:
    """A class representing a square.

    This class is serving a functionality related to squares.

    Attributes:
    __size (int): the size of the square
    """
    def __init__(self, size=0):
        """Initialize a Square instance.

        Args:
            size (int): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """Retrieve the size attribute

        Returns:
            the size attribute
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the value of attribute size

         Args:
            value (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calclating square area

        Returns:
            the area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """prints in stdout the square with the character #"""
        if (self.__size == 0):
            print()
        else:
            for _ in range(self.__size):
                print('#' * self.__size)
