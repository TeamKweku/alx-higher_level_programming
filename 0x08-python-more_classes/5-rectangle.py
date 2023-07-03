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

    def area(self):
        """
        Calculates the area of the rectangle

        Args:
            width(int): width of the rectangle
            height(int): height of the rectangle

        Returns:
            int: area of the rectangle
        """

        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle

        Args:
            width: the width of rectangle
            height: height of rectangle

        Returns:
            int: 0 if width or height is 0
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle_str = ""

        for _ in range(self.__height):
            rectangle_str += "#" * self.__width + "\n"
        return rectangle_str.rstrip()

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        print("Bye rectangle...")
