#!/usr/bin/python3
"""
Module that contain student class
"""


class Student:
    """
    class that identifies a Student

    Attributes:
    first_name: the first name of student
    last_name: the last name of student
    age: student age
    """
    def __init__(self, first_name, last_name, age):
        """
        instantiation function
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, list=["first_name", "last_name", "age"]):
        """
        retrieves a dictionary representation of a Student instance
        """
        my_dict = {}
        for value in list:
            if value in ["first_name", "last_name", "age"]:
                my_dict[value] = getattr(self, value)
        return my_dict

    def reload_from_json(self, json):
        """
        replaces all attributes of the Student instance
        """
        for key in json:
            setattr(self, key, json[key])
