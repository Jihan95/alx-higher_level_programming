#!/usr/bin/python3
"""
Module to contain the “base” of all other classes in this project
"""
from json import dumps, loads
from os.path import isfile


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return '[]'
        return str(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of list_objs

        Args:
        list_objs: a list of instances who inherits of Base
        """
        filename = '{}.json'.format(cls.__name__)
        lis = []
        for obj in list_objs:
            lis.append(obj.to_dictionary())
        with open(filename, 'w') as f:
            f.write(cls.to_json_string(lis))

    @staticmethod
    def from_json_string(json_string):
        """
        returns the list of the JSON string representation json_string
        """
        if json_string is None or len(json_string) == 0:
            return []
        return loads(json_string.replace("'", "\""))

    @classmethod
    def create(cls, **dictionary):
        """
        returns an instance with all attributes already set

        Args:
        **dictionary: instance attributes
        """
        instance = cls(10, 7, 0, 0)
        if cls.__name__ == 'Rectangle':
            cls.update(
                    instance,
                    id=dictionary['id'],
                    x=dictionary['x'],
                    y=dictionary['y'],
                    width=dictionary['width'],
                    height=dictionary['height']
                    )
        else:
            cls.update(
                    instance,
                    id=dictionary['id'],
                    x=dictionary['x'],
                    y=dictionary['y'],
                    size=dictionary['size']
                    )
        return instance

    @classmethod
    def load_from_file(cls):
        """
        returns a list of instances
        """
        filename = '{}.json'.format(cls.__name__)
        lis = []
        if isfile(filename):
            with open(filename, 'r') as f:
                data = f.read()
        else:
            return lis
        tr_data = cls.from_json_string(data)
        for item in tr_data:
            lis.append(cls.create(**item))
        return lis
