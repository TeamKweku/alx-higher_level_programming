#!/usr/bin/python3
"""A module that defines a class MyInt that inherites
    from the int class
    """


class MyInt(int):
    """
    creates a class that reinvents the __eq__ and __ne__
    magic methods
    """

    def __eq__(self, other):
        """
        function overides the == operator

        Args:
            other: the object to compare with

        Returns:
            bool: True if value are not equal and False otherwise
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        function overides the != operator

        Args:
            other: the object to compare with

        Returns:
            bool: True is the values are equal and False otherwise
        """
        return super().__eq__(other)
