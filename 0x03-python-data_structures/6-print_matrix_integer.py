#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for m in i:
            print("{:d}" .format(m), end=" " if m != i[-1] else "")
        print()
