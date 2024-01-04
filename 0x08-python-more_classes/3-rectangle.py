#!/usr/bin/python3
"""
Module contains a class defination
"""


class Rectangle:
    """
    A class representing a rectangle

    This class is serving a functionality related to rectangles

    Attributes:
    __width (int): the width of the rectangle
    __height (int): the height of the rectangle
    """
    def __init__(self, width=0, height=0):
        """
        Method to initialize a Rectangle instance

        Args:
        -width (int): the Rectangle object width
        -height (int): the Rectangle object height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Retrieves the width attribute

        Returns:
            the object width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        sets the width attribute

        Args:
            value (int): the width of the rectangle

        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Retrieves the height attribute

        Returns:
            the object height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        sets the height attribute

        Args:
            value (int): the height of the rectangle

        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculates the rectangle area

        Returns:
            the rectangle area
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates the rectangle perimeter

        Returns:
            the rectangle perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__width * 2 + self.__height * 2

    def __str__(self):
        """
        Returns the rectangle with the character #
        """
        rect_str = ''
        if self.__width == 0 or self.__height == 0:
            return rect_str
        for _ in range(self.__height - 1):
            rect_str += '#' * self.__width + '\n'
        rect_str += '#' * self.__width
        return rect_str
