#!/usr/bin/python3
""" This is a module for a class definition of a rectangle"""


class Rectangle:
    """This is the implementation of a class rectangle

    Attributes:
        width(int): the width of the rectangle
        height(int): the height of the rectangle
    """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """Gets the width of the rectangle

        Returns:
            int: width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle

        Args:
            value(int): the width of the rectangle

        Raises:
            TypeError: if `value` is not an integer
            ValueError: if `value` is less than 0
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """
        Gets the height of the rectangle

        Returns:
            int: the height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle

        Args:
            value(int): the height of the rectangle

        Raises:
            TypeError: if `value` is not an integer
            ValueError: is `value` is less than 0
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
