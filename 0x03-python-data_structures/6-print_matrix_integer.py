#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """Prints a matrix of integers"""
    for row in matrix:
        for item in row:
            if item == row[-1]:
                print("{:d}".format(item), end='')
            else:
                print("{:d}".format(item), end=" ")
        print()
