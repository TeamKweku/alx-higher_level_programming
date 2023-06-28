#!/usr/bin/python3
"""This is a module for a class definition of a square"""


class Square:
    """This is an implementation of a class square

    Attributes:
        size(int): the size of square
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Intializes an instance of a square class

        Args:
            size(int, optional): size of the square (default: size = 0)

        Raises:
            TypeError: if `size` is not an integer
            ValueError: if `size` is less than 0
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        Gets the position attribute of the class square

        Returns:
            tuple: 2 args tuple
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square

        Args:
            value(tuple): 2 value tuple

        Raises:
            TypeError: if `value` is not a tuple
        """
        if (type(value) is not tuple
                or len(value) != 2
                or not all(type(num) is int for num in value)
                or not all(int(num) >= 0 for num in value)
                ):
            raise TypeError("position must be a tuple of 2 positive integer")
        else:
            self.__position = value

    def area(self):
        """
        method that calculates the square of size and returns val

        Args:
            size: self.__size

        Returns:
            square of size
        """
        return self.__size**2

    def my_print(self):
        """
        method that prints in stdout the square with the character
        `#`

        Args:
            size: self.__size ** 2
            position: tuple of 2 values
        """
        if self.__size == 0:
            print("")
            return
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for j in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()
