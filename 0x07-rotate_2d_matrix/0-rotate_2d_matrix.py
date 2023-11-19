#!/usr/bin/python3

"""
Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """
    - Given an n x n 2D matrix, rotate it 90 degrees clockwise.
    - Do not return anythng.
    """

    n = len(matrix[0])

    for i in range(n - 1, -1, -1):
        for j in range(0, n):
            matrix[j].append(matrix[i].pop(0))
