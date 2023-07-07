#!/usr/bin/python3
"""A module that adds two integers together"""


def add_integer(a, b=98):
    """
    a function that adds two integers

    Args:
        a(int): first integer
        b(int): second integer

    Raises:
        TypeError: is a or b is not an integer

    Return:
        int: returns sum of two integers
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
