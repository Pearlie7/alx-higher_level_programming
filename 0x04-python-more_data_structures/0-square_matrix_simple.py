#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_mat = []
    if len(matrix) == 0:
        return new_mat

    new_lst = [[i*i for i in j] for j in matrix]
    return new_mat
