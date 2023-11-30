#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for idx, num in enumerate(i):
            if idx == len(i) - 1:
                print("{:d}".format(num), end="")
            else:
                print("{:d}".format(num), end=" ")
        print()
