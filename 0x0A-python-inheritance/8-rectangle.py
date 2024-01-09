#!/usr/bin/python3
"""
Module that contain an BaseGeometry class
and a recatangle class
"""


BaseGeometry = _import_('7-base_geometry').BaseGeometry


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
