#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_cpy = [row[:] for row in matrix]
    if (matrix is None):
        return
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix_cpy[i][j] = matrix[i][j] ** 2
    return (matrix_cpy)
