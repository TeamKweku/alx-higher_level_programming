#!/usr/bin/python3
"""a module that implements a class Square that inherits
    from Rectangle class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """This is an implementation of a class Square

    Attributes:
        size(int): the size of the square
    """
    def __init__(self, size):
        """
        Initializes an instance of a square class

        Args:
            size(int): size of the square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
