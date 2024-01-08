#!/usr/bin/python3
"""
Module that contain an BaseGeometry class
and a recatangle class
"""


class BaseGeometry():
    """
    an abstract class for any geometry shape
    """
    def area(self):
        """
        unimplemented function
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Function to validate an integer

        Args:
        - name (string): the name of geometry
        - value (int): value to be validated

        Raises:
        TypeError: if value isn't an integer
        ValueError: if value is less than or equal 0
        """
        if type(name) != str:
            raise TypeError("{} must be a string".format(name))
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    A class that represents a rectangle

    Attributes:
    -height (int): the height of the rectangle
    -width (int): the width of the rectangle
    """
    def __init__(self, width, height):
        """
        Fanction that instantiate a Rectangle object
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Function to calculate rectangle area
        """
        return self.__width * self.__height

    def __str__(self):
        """
        retrun the rectangle in shape:
        [Rectangle] <width>/<height>
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
