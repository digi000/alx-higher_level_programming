#!/usr/bin/python3
""" function that divides all elements of a matrix."""
def matrix_divided(matrix, div):
    """ function that divides all elements of a matrix."""
    for i in matrix:
        for j in i:
            if not isinstance(j, int) and not isinstance(j, float):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    r1 = len(matrix[0])
    r2 = len(matrix[1])
    if r1 != r2:
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(j / div, 2) for j in i] for i in matrix]
