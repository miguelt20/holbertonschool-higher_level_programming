#!/usr/bin/python3
def power(num):
    num = num ** 2
    return num


def square_matrix_simple(matrix=[]):
    counter = 0
    new_matrix = []
    for row in matrix:
        new_matrix.append(list(map(power, matrix[counter])))
        counter = counter + 1
    return new_matrix
