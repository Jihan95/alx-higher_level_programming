#!/usr/bin/python3
"""
This modules contains rectangle class
"""


from models.base import Base


class Rectangle(Base):
    """
    A class that represents a rectangle

    Attributes:
    __width (int): the width of the rectangle
    __height (int): the height of the rectangle
    __x : the rectangle position x
    __y: the rectangle position y
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        the object instantiation function
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        retrieves the instance width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        sets the value of the object width
        """
        self.validate_attribute('width', value)
        self.__width = value

    @property
    def height(self):
        """
        retrieves the instance height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        sets the value of the object height
        """
        self.validate_attribute('height', value)
        self.__height = value

    @property
    def x(self):
        """
        retrieves the x position of an object
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        sets the value of the x position of the object
        """
        self.validate_attribute('x', value)
        self.__x = value

    @property
    def y(self):
        """
        retrieves the y position of an object
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        sets the value of the y position of the object
        """
        self.validate_attribute('y', value)
        self.__y = value

    def validate_attribute(self, name, value):
        """
        Function to validate an integer

        Args:
        - name (string): the name of attribute
        - value (int): value to be validated

        Raises:
        TypeError: if value isn't an integer
        ValueError: if value is less than or equal 0
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if name in ['width', 'height'] and value <= 0:
            raise ValueError("{} must be > 0".format(name))
        if name in ['x', 'y'] and value < 0:
            raise ValueError("{} must be >= 0".format(name))

    def area(self):
        """
        Function to calculate the rectangle area

        Returns:
        the area of the rectangle
        """
        return self.__width * self.__height

    def display(self):
        """
        Function to display a rectangle
        """
        for _ in range(self.__height):
            print('#' * self.__width)

    def __str__(self):
        """
        Function to return string representation of an object
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id,
                self.__x,
                self.__y,
                self.__width,
                self.__height
                )
