#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """ function that add 2 tuples

        Args:
            tuple_a = first tuple
            tuple_b = second tuple

        Returns:
            return value. new tuple
    """
    a = tuple_a[:2] + (0, 0)
    b = tuple_b[:2] + (0, 0)

    result = (a[0] + b[0], a[1] + b[1])

    return (result)
