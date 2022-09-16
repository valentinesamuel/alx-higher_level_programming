#!/usr/bin/python3
"""
    lazy_matrix_mul: multiply 2 matrices
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """ Multiply 2 matrices together, a and b
    Args:
    m_a (list): first matrix
    m_b (list): second matrix
    """

    return np.matmul(m_a, m_b)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/101-lazy_matrix_mul.txt")
