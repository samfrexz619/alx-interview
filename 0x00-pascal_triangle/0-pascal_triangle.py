#!/usr/bin/python3
"""function for Pascal's Triangle"""


def pascal_triangle(n):
    """
    lists of integers
    representing the Pascal’s triangle
    """
    if n <= 0:
        return []

    triangle = [[1]]
    while len(triangle) != n:
        previous = triangle[-1]
        current = [1]
        for idx in range(len(previous) - 1):
            current.append(previous[idx] + previous[idx + 1])
        current.append(1)
        triangle.append(current)
    return triangle
