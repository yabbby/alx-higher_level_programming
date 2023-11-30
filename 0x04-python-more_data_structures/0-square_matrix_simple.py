#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_mat = []
    for row in matrix:
        tmp = []
        for num in row:
            tmp.append(num ** 2)
        new_mat.append(tmp)

    return new_mat
