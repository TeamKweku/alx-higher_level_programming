#!/usr/bin/python3
""" This is a module for a class definition of a square"""


class Square:
    """This is an implementation of a class square

    Attributes:
        size(int): the size of a square.
    """

    def __init__(self, size=0):
        """
        Intializes an instance of a square class

        Args:
            size(int, optional): size of the square (default: size = 0)

        Raises:
            TypeError: if `size` is not an integer
            ValueError: if `size` is less than 0
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
