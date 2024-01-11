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
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(' ' * self.__x, end='')
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

    def update(self, *args, **kwargs):
        """
        Function to update object attributes
        args arrangement:
        1st argument should be the id attribute
        2nd argument should be the width attribute
        3rd argument should be the height attribute
        4th argument should be the x attribute
        5th argument should be the y attribute
        """
        attributes = ['id', 'width', 'height', 'x', 'y']
        if len(args) > 0:
            for i in range(len(args)):
                setattr(self, attributes[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Function that returns the dictionary representation of a Rectangle
        """
        return {
                "id" : self.id,
                "width" : self.width,
                "height" : self.height,
                "x" : self.x,
                "y" : self.y
                }
