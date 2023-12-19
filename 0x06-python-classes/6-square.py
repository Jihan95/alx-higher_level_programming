#!/usr/bin/python3
"""This module contains a class definition for representing squares."""


class Square:
    """A class representing a square.

    This class is serving a functionality related to squares.

    Attributes:
    __size (int): the size of the square
    __position (tuple): position of two integers
    """
    def __init__(self, size=0, position=(0, 0)):
        """Initialize a Square instance.

        Args:
            size (int): The size of the square. Defaults to 0.
            position (tuple): the position of two integers. Defaults to (0, 0).
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Retrieve the position

        Returns:
            the position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the value of position

         Args:
            value (int): The position value

        Raises:
            TypeError: if position is not a tuple of its
            values are not integers
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Calclating square area

        Returns:
            the area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(' ' * self.__position[0], end='')
                print('#' * self.__size)
