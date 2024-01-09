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

    def to_json(self):
        """
        retrieves a dictionary representation of a Student instance
        """
        return {
                "first_name": self.first_name,
                "last_name": self.last_name,
                "age": self.age
                }
