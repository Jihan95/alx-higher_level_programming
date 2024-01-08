#!/usr/bin/python3
"""
This module contains matrix_div function
"""


def matrix_divided(matrix, div):
    """
    This function divides all ememnts of matrix by a number

    Parameters:
    - matrix: the matrix requires to be divided
    - div: the division number

    Returns:
    The divided matrix
    """
    err = "matrix must be a matrix (list of lists) of integers/floats"
    if matrix is None and div is None:
        raise TypeError(" matrix_divided() missing 2 required positional"
                        "arguments: 'matrix' and 'div'")
    if div is None:
        raise TypeError("matrix_divided() missing 1 required positional"
                        "argument: 'div'")
    if div == float('inf') or div == -float('inf'):
        return [[ 0.0 for item in row] for row in matrix]
    res_matrix = []
    row_len = len(matrix[0])
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(err)
        else:
            for x in row:
                if type(x) not in [int, float]:
                    raise TypeError(err)
        if len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for row in matrix:
        res_matrix.append([round(element/div, 2) for element in row])
    return res_matrix
