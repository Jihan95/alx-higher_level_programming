#!/usr/bin/python3
"""
Module that contain an BaseGeometry class
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
        if value is None:
            raise TypeError("integer_validator() missing 1 required positional"
                            " argument: 'value'")
        if value is None and name is None:
            raise TypeError("integer_validator() missing 2 required positional"
                            " arguments: 'name' and 'value'")
        if type(name) != str:
            raise TypeError("{} must be a string".format(name))
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
