#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    a = []
    for i in matrix:
        b = []
        for j in i:
            m = j * j
            b.append(m)
        a.append(b)
    return (a)
