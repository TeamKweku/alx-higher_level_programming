#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    result = [list(map(lambda x: x ** 2, row)) for row in matrix]
    return (result)
