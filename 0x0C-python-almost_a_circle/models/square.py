#!/usr/bin/python3
"""
Module that represents a square
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    class that represents a square
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        The constructor function of the class
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Function to return string representation for an object
        """
        return "[Square] ({}) {}/{} - {}".format(
                self.id,
                self.x,
                self.y,
                self.width
                )

    @property
    def size(self):
        """
        Function to retrieve the size of the square
        """
        return self.width

    @size.setter
    def size(self, size):
        """
        Function to initialze the size of the square
        """
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """
        Function to update object attributes
        args arrangement:
        1st argument should be the id attribute
        2nd argument should be the size attribute
        3rd argument should be the x attribute
        4th argument should be the y attribute
        """
        attributes = ['id', 'size', 'x', 'y']
        if len(args) > 0:
            for i in range(len(args)):
                setattr(self, attributes[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Function that returns the dictionary representation of a Square
        """
        return {
                "id" : self.id,
                "size" : self.size,
                "x" : self.x,
                "y" : self.y
                }
