#!/usr/bin/python3
"""
Module to perform matrix multiplication
"""


def matrix_mul(m_a, m_b):
    """
    Function to multiply two matrices
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a lisst of lists")
    if m_a == [] or all(row == [] for row in m_a):
        raise ValueError("m_a can't be empty")
    if m_b == [] or all(row == [] for row in m_b):
        raise ValueError("m_b can't be empty")
    if not all(isinstance(num, (int, float)) for row in m_a for num in row):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(num, (int, float)) for row in m_b for num in row):
        raise TypeError("m_b should contain only intgers or floats")
    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m=b):
        raise ValueErrpr("m_a and m_b can't be multiplied")

    # Matrix multiplication logic
    rows_a = len(m_a)
    cols_a = len(m_a[0])
    cols_b = len(m_b[0])
    result = [[0 for _ in range(cols_b)] for _ in range(rows_a)]

    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                results[i][j] += m_a[i][k] * m_b[k][j]

    return result
