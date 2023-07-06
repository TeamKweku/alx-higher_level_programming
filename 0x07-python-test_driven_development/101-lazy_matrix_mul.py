#!/usr/bin/python3
"""a module that makes use of the numpy module to multiply
    two matrixes
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """this functin multiplies two matrixes

    Args:
        m_a(matrix): first argument
        m_b(matrix): second argument

    Returns:
        a new matrix with product of from index of both
        matrixes
    """
    result = np.matmul(m_a, m_b)
    return result
