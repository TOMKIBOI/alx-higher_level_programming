#!/usr/bin/python3
"""
Create a function def pascal_triangle(n): that
returns a list of lists of integer
representing the Pascal’s triangle of n
"""


def pascal_triangle(n):
    """returns a list of lists of integer"""
    if n <= 0:
        return []

    def binomial_coefficient(n, m):
        if m == 0 or m == n:
            return 1
        result = 1
        for i in range(1, m + 1):
            result = result * (n - i + 1) // i
        return result

    triangle = []
    for i in range(n):
        row = [binomial_coefficient(i, j) for j in range(i + 1)]
        triangle.append(row)

    return triangle
