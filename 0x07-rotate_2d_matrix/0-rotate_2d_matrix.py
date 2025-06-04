#!/usr/bin/env python3
"""
Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """
    Rotate a 2D matrix 90 degrees clockwise in place.
    This function modifies the input matrix in place to achieve the rotation.
    :param matrix: List of lists representing the 2D matrix to be rotated.
    :return: None
    """
    n = len(matrix)

    for i in range(n):
        for j in range(i+1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for row in matrix:
        row.reverse()
    return matrix

    for row in matrix:
        print(" ".join(str(x) for x in row))
