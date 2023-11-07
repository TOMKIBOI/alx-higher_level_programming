#!/usr/bin/python3
"""
Create a function def pascal_triangle(n): that 
returns a list of lists of integers representing the Pascal’s triangle of n
"""


def pascal_triangle(n):
    """Represent Pascal's Triangle of size n.
    Returns a list of lists of integers representing the triangle.
    """
    if x <= 0:
        return []
    triangle = [[1]]
    while len(triangle) != x:
        trin = triangle[-1]
        temp = [1]
        for i in range(len(trin) - 1):
            temp.append(trin[i] + trin[i + 1])
        temp.append(1)
        triangle.append(temp)
    return triangle
