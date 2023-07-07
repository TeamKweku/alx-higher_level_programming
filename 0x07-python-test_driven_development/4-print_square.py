#!/usr/bin/python3
""" a module the prints a size of a square"""


def print_square(size):
    """
    a function that prints the size of a a sqare with character '#'

    Args:
        size(int): size of the printed square

    Raises:
        TypeError: if `size` is not an integer or float and less than 0
        ValueError: if `size` is not greater than 0
    """
    if not isinstance(size, (int, float)):
        raise TypeError("size must be an integer")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    size = int(size)

    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
