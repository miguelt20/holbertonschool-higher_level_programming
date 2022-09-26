#!/usr/bin/python3
def power(num):
    num = num ** 2
    return num
def square_matrix_simple(matrix=[]):
    new_matrix = []
    new_matrix.append(list(map(power, matrix[0])))
    new_matrix.append(list(map(power, matrix[1])))
    new_matrix.append(list(map(power, matrix[2])))
    return new_matrix
