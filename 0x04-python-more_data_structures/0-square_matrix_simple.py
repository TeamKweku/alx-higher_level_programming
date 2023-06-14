#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """ Function that computes squares of all ints of a matrix

        Args:
            matrix: 2 dimensional array
        Returns:
            return value. new_matrix with squared ints
    """
    if not matrix:
        return (None)
    new_matrix = [[num ** 2 for num in row] for row in matrix]
    return (new_matrix)
