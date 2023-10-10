#!/usr/bin/python3
"""Defines Pascal's Triangle function."""


def pascal_triangle(n):
    """Represent Pascal's Triangle with size n.
    Returns a list of lists of integers that represent the triangle.
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        trim = triangles[-1]
        tmp = [1]
        for i in range(len(trim) - 1):
            tmp.append(trim[i] + trim[i + 1])
        tmp.append(1)
        triangles.append(tmp)
    return triangles
