#!/usr/bin/python3
"""a module that defines Rectangle class that inherits from BaseGeometry. """
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """a class that inherits from the BaseGeometry class"""

    def __init__(self, width, height):
        """method initializes variables of the instance

        Args:
            width(int): the width of the Rectangle
            height(int): the height of the Rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

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

    def __str__(self):
        """Return the print() and str() representation of a Rectangle"""
        return f"[Rectangle] {self.__width}/{self.__height}"
