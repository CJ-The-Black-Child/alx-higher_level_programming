#!/usr/bin/python3


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices.

    Args:
    m_a (list): Matrix A represented as a list of lists of integers or floats.
    m_b (list): Matrix B represented as a list of lists of integers of floats.

    Returns:
        list: Resultant matrix after multiplying matrix A with matrix B.

    Raises:
    TypeError: If m_a or m_b is not a list or nort a list of lists.
    ValueError: If m_a or m_b is empty ([] or [[]]).
    TypeError: If an element in m_a or m_b is not an integer or float.
    TypeError: If m_a or m_b is not a rectangle (rpws with different sizes).
    ValueError: if m_a and m_b cannot be multiplied.

    """

    # Validate m_a and m_b
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a must be a list and m_b must be a list")
    if not all(isinstance(row, list) for row in m_a) \
            or not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_a must be a list of lists and m_b must be a list of lists")
    if len(m_a) == 0 or len(m_b) == 0:
        raise ValueError("m_a can't be empty and m_b can't be empty")
    if not all(isinstance(num, (int, float)) for row in m_a for num in row) \
            or not all(isinstance(num, (int, float)) for row in m_b for num in row):
        raise TypeError("m_a should contain only integers or floats and m_b should contain only integers or floats")
    if len(set(len(row) for row in m_a)) > 1 or len(set(len(row)
                for row in m_b)) > 1:
        raise TypeError("each row of m_a must be of the same size and each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Perform matrix multiplication
    result = []
    for i in range(len(m_a)):
        row = []
        for j in range(len(m_b[0])):
            sum_val = 0
            for k in range(len(m_b)):
                sum_val += m_a[i][k] * m_b[k][j]
            row.append(sum_val)
        result.append(row)

    return result
