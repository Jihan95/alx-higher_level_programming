#!/usr/bin/python3
"""
Module to product two matrices
"""


def matrix_mul(m_a, m_b):
    """
    Function to multiply two matrices

    Parameters:
    -m_a: the first matrix
    -m_b: the second matrix
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if len(m_a) != 0:
        nca = len(m_a[0])
    fa, nra, fan = 0, 0, 0
    for row in m_a:
        if not isinstance(row, list):
            raise TypeError("m_a must be a list of lists")
        else:
            nra += 1
            if nca != len(row):
                fa = 1
            for x in row:
                if (type(x) not in [int, float]) and fan == 0:
                    fan = 1
    if len(m_b) != 0:
        ncb = len(m_b[0])
    fb, nrb, fbn = 0, 0, 0
    for row in m_b:
        if not isinstance(row, list):
            raise TypeError("m_b must be a list of lists")
        else:
            nrb += 1
            if ncb != len(row):
                fb = 1
            for x in row:
                if (type(x) not in [int, float]) and fbn == 0:
                    fbn = 1
    if (len(m_a) == 0) or (len(m_a) == 1 and len(m_a[0]) == 0):
        raise ValueError("m_a can't be empty")
    if (len(m_b) == 0) or (len(m_b) == 1 and len(m_b[0]) == 0):
        raise ValueError("m_b can't be empty")
    if fan == 1:
        raise TypeError("m_a should contain only integers or floats")
    if fbn == 1:
        raise TypeError("m_b should contain only integers or floats")
    if fa == 1:
        raise TypeError("each row of m_a must be of the same size")
    if fb == 1:
        raise TypeError("each row of m_b must be of the same size")
    if nca != nrb:
        raise ValueError("m_a and m_b can't be multiplied")
    c = [[0 for _ in range(len(m_b[0]))] for _ in range(len(m_a))]
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for n in range(len(m_b)):
                c[i][j] += m_a[i][n] * m_b[n][j]
                if isinstance(c[i][j], float):
                    c[i][j] = round(c[i][j], 2)
    return c
