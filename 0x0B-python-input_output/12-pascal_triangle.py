#!/usr/bin/python3
"""
Module that contain function to calculate pascal triangle
"""


def pascal_triangle(n):
    """
    Function to calculate pascal trangle

    Args:
    n (int): number of rows of the triangle

    Return:
    list of lists of pascal trangle values
    """
    pas_tr = []
    if n <= 0:
        return pas_tr
    for i in range(n):
        row = [1] * (i + 1)
        pas_tr.append(row)
    for i in range(n):
        if i > 1:
            for j in range(1, i):
                pas_tr[i][j] = pas_tr[i - 1][j - 1] + pas_tr[i - 1][j]
    return pas_tr
