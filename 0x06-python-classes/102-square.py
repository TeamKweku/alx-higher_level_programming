#!/usr/bin/python3
"""This is a module for a class definition of a square"""


class Square:
    """This is an implementation of a class square

    Attributes:
        size(int): the size of square
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

    @property
    def size(self):
        """
        Gets thesize of the square

        Returns:
            int: the size of the square
        """

        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square

        Args:
            value(int): the size of the square

        Raises:
            TypeError: if `value` is not an integer
            ValueError: if `value` is less than 0
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """
        method that calculates the square of size and returns val

        Args:
            size: self.__size

        Returns:
            square of size
        """
        return self.__size**2

    def __eq__(self, other):
        """Defines the comparator for == (equal)"""
        return self.area() == other.area()

    def __ne__(self, other):
        """Define the comparator for != (not equal)"""
        return self.area() != other.area()

    def __gt__(self, other):
        """Define the comparator for > (greater than)"""
        return self.area() > other.area()

    def __ge__(self, other):
        """Define the comparator for >= (greater or equal)"""
        return self.area() >= other.area()

    def __lt__(self, other):
        """Define comparator for < (less than)"""
        return self.area() < other.area()

    def __le__(self, other):
        """Define the comparator for <= (less than or equals)"""
        return self.area() <= other.area()
