#!/usr/bin/python3
"""
module to multiply two matrices using numpy
"""


import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Function to multiply two matrices using numpy

    Parameters:
    - m_a: the first matrix
    - m_b: the second matrix
    """
    if not isinstance(m_a, list):
        raise TypeError("first argument must be a list of lists")
    if not isinstance(m_b, list):
        raise TypeError("second argument must be a list of lists")
    if len(m_a) != 0:
        nca = len(m_a[0])
    fa, nra, fan = 0, 0, 0
    for row in m_a:
        if not isinstance(row, list):
            raise TypeError("first argument must be a list of lists")
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
            raise TypeError("second argument must be a list of lists")
        else:
            nrb += 1
            if ncb != len(row):
                fb = 1
            for x in row:
                if (type(x) not in [int, float]) and fbn == 0:
                    fbn = 1
    if (len(m_a) == 0) or (len(m_a) == 1 and len(m_a[0]) == 0):
        raise ValueError("first matrix can't be empty")
    if (len(m_b) == 0) or (len(m_b) == 1 and len(m_b[0]) == 0):
        raise ValueError("second matrix can't be empty")
    if fan == 1:
        raise TypeError("first matrix should contain only integers or floats")
    if fbn == 1:
        raise TypeError("second matrix should contain only integers or floats")
    if fa == 1:
        raise TypeError("all rows of first matrix must be of the same size")
    if fb == 1:
        raise TypeError("all rows of second matrix must be of the same size")
    if nca != nrb:
        raise ValueError("two matrices can't be multiplied")
    a = np.array(m_a)
    b = np.array(m_b)
    c = np.dot(a, b)
    return c
