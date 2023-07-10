#!/usr/bin/python3
"""a module that defines an empty class BaseGeometry"""


class BaseGeometry:
    """This is the implementation of a class BaseGeometry"""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """function that validates a value if its int

        Arguments:
            name(str): name of the passed value
            value(int): an integer value

        Raises:
            TypeError: if value passed is not an int
            ValueError: if the value passed is less than or
                equal to 0
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
