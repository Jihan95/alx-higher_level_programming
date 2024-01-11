#!/usr/bin/python3
"""
Module to contain the “base” of all other classes in this project
"""


class Base:
    """
    This class will be the “base” of all other classes in this project.
    The goal of it is to manage id attribute in all your future classes
    and to avoid duplicating the same code (by extension, same bugs)

    Attributes:
    __nb_objects (int): number of objects instantiated of the class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        The instantiation function

        Args:
        id (int): the object id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
