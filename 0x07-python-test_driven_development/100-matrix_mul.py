#!/usr/bin/python3
"""a module that mutilplies two matrixes and returns the product
    in a new matrx
"""


def matrix_mul(m_a, m_b):
    """
    function that multiplies two matrixes and returns the product as
    a new matrix

    Args:
        m_a(matrix(int, float)): first argument
        m_b(matrix(int, float)): second argument

    Raises:
        TypeError: if m_a or m_b is not a list or if any of them is not
            a list of lists
            if one element of those list of lists is not an integer
            or a float
            if m_a or m_b is not a rectangle (all ‘rows’ should be
            of the same size)
        ValueError: if m_a or m_b is empty([] or [[]])
            or If m_a and m_b can’t be multiplied
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    if not all(isinstance(num, (int, float)) for row in m_a for num in row):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(num, (int, float)) for row in m_b for num in row):
        raise TypeError("m_b should contain only integers or floats")
    if len(set(len(row) for row in m_a)) > 1:
        raise TypeError("each row of m_a must be of the same size")
    if len(set(len(row) for row in m_b)) > 1:
        raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = []
    for i in range(len(m_a)):
        row = []
        for j in range(len(m_b[0])):
            elem = 0
            for k in range(len(m_b)):
                elem += m_a[i][k] * m_b[k][j]
            row.append(elem)
        result.append(row)

    return result
