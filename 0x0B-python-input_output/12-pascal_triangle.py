#!/usr/bin/python3
"""
Module that contains a function
that returns a list of lists of integers
representing the Pascal's triangle
"""


def pascal_triangle(n):
    """ Pascal's triangle """

    if n <= 0:
        return []

    t_pascal = [[1]]
    while len(t_pascal) != n:
        prev = t_pascal[-1]
        tmp = [1]
        for i in range(len(prev) - 1):
            tmp.append(prev[i] + prev[i + 1])
        tmp.append(1)
        t_pascal.append(tmp)
    return t_pascal
