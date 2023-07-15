#!/usr/bin/python3
"""a module that defines a rectangle class that inherites from base class"""
from models.base import Base


class Rectangle(Base):
    """
    a class that defines a rectangle

    Attributes:
        width(int): the width of the rectangle
        height(int): the height of the rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

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

        if value <= 0:
            raise ValueError("width must be > 0")

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

        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """
        Returns x of the rectangle
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        sets x of the rectangle instance

        Args:
            value(int): x value
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")

        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """
        Returns value of y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Sets the value of y

        Args:
            value(int): value of y
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")

        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value
