#!/usr/bin/python3
"""a module that implements a pascal_triangle function"""


def pascal_triangle(n):
    """
    function that returns a list of list of ints representing
    the Pascal's triangle.

    Args:
        n(int): the number to be printed
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)

    return triangle
