import numpy as np

def commutator(matrix_1, matrix_2):
    return np.dot(matrix_1, matrix_2) - np.dot(matrix_2, matrix_1)

def anticommutator(matrix_1, matrix_2):
    return np.dot(matrix_1, matrix_2) + np.dot(matrix_2, matrix_1)

def find_matrix_mask(input_matrix):
    input_matrix_mask = input_matrix !=0
    return input_matrix_mask