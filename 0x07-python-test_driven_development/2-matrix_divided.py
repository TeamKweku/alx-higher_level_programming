#!/usr/bin/python3
""" A module that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """
    function that divides all elements of a matrix

    Args:
        matrix(int, float): matrix passed to the function
        div(int, float): an int value to divide by

    Return:
        new_matrix: containing elements of the divided by div

    Raises:
        TypeError: if `matrix` is not a list of list of ints or floats
        or each row of the matrix is not the same size or div is not an int

        ZeroDivisionError: if div is equal 0
    """
    if not isinstance(matrix, list) or any(not isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    for row in matrix:
        if any(not isinstance(elem, (int, float)) for elem in row):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(element / div, 2) for element in row] for row in matrix]
