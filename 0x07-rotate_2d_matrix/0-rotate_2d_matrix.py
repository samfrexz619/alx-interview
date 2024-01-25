#!/usr/bin/python3
"""
Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """
    Rotate a 2D matrix 90 degrees clockwise.
    """
    for idx in range(int(len(matrix) / 2)):
        for j in range(idx, (len(matrix) - idx - 1)):
            x = (len(matrix) - 1 - j)
            tmp = matrix[idx][j]
            matrix[idx][j] = matrix[x][idx]
            matrix[x][idx] = matrix[(len(matrix) - idx - 1)][x]
            matrix[(len(matrix) - idx - 1)][x] = matrix[j][(len(matrix) - idx - 1)]
            matrix[j][(len(matrix) - idx - 1)] = tmp
