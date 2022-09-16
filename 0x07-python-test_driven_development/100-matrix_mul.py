#!/usr/bin/python3
"""
    Multiply 2 matrices
"""


def matrix_mul(m_a, m_b):
    """
    Multiplies two matrices together
    Args:
        m_a (list): matrix of numbers
        m_b (list): matrix of numbers
    """

    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")

    for row in m_a:
        if type(row) is not list:
            raise TypeError("m_a must be a list of lists")
    for row in m_b:
        if type(row) is not list:
            raise TypeError("m_b must be a list of lists")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    for r in m_a:
        for c in r:
            if not (type(c) is int or type(c) is float):
                raise TypeError("m_a should contain only integers or floats")
    for r in m_b:
        for c in r:
            if not (type(c) is int or type(c) is float):
                raise TypeError("m_b should contain only integers or floats")

    rowA = len(m_a)
    colA = len(m_a[0])
    rowB = len(m_b)
    colB = len(m_b[0])

    for r in m_a:
        if len(r) != colA:
            raise TypeError("each row of m_a must should be of the same size")

    for r in m_b:
        if len(r) != colB:
            raise TypeError("each row of m_b must should be of the same size")

    if colA != rowB or rowA != colB:
        raise ValueError("m_a and m_b can't be multiplied")

    result = [[0 for row in range(colB)] for col in range(rowA)]

    for i in range(rowA):
        for j in range(colB):
            for k in range(colA):
                result[i][j] += m_a[i][k] * m_b[k][j]

    return result
