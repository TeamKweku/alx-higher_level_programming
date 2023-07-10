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
