"""
    Created by Maciej Winczewski on April 2021
    for subject named "Metody Numeryczne"
    All rights reserved

    File storing function implements lu factorization
    to solve linear system equations.
"""

from copy import deepcopy

from typing import List


def lu_factorization(a_matrix, b_vector):
    """ solve system of linear equations in form
        a_matrix * x_vector = b_vector
        using LU factorization method

        @:param a_matrix
        @:param b_vector
        @:return x_vector """

    m_size, n_size = len(a_matrix), len(a_matrix[0])
    u_matrix = deepcopy(a_matrix)
    l_matrix = eye(n_size)
    perm_matrix = eye(n_size)

    # check is pivoting needed
    for i in range(m_size-1):

        # find index and max element in u_matrix, where every element is equal abs(element)
        abs_nbs = []
        for row in u_matrix[i:m_size]:
            abs_nbs.append(abs(row[i]))

        # determine the maximum element and his index
        pivot, ind = my_max(abs_nbs)
        ind = ind+i

        # swap rows in matrices
        swap(u_matrix, i, ind, i, m_size+1)
        swap(l_matrix, i, ind, 0, i)
        swap(perm_matrix, i, ind, 0, len(perm_matrix))

        # calculate some l_matrix and u_matrix elements
        for j in range(i+1, m_size):
            l_matrix[j][i] = u_matrix[j][i] / u_matrix[i][i]
            u_matrix[j][i:m_size] = sub_vectors(u_matrix[j][i:m_size],
                                                multiply_vector_by_scalar(u_matrix[i][i:m_size], l_matrix[j][i]))

    # b = b * perm_matrix
    b_vector = multiply_matrix_by_vector(perm_matrix, b_vector)

    # calculate y vector using forward substitution where U * y = b
    y_vector = [1.0 for i in range(n_size)]
    for i in range(n_size):
        sum = 0.0
        for j in range(i):
            sum += l_matrix[i][j] * y_vector[j]
        y_vector[i] = (b_vector[i] - sum)

    # calculate x vector using back substitution where L * x = y
    x_vector = [1.0 for i in range(n_size)]
    for i in range(n_size-1, -1, -1):
        sum = 0.0
        for j in range(i+1, n_size):
            sum += u_matrix[i][j] * x_vector[j]
        x_vector[i] = (y_vector[i] - sum) / u_matrix[i][i]

    return x_vector


# --------------
# NEEDED METHODS
# --------------

def my_max(vector):
    """ find max element in vector """
    max_nb = vector[0]
    max_ind = 0

    for ind, nb in enumerate(vector):
        if nb > max_nb:
            max_nb = nb
            max_ind = ind

    return max_nb, max_ind


def swap(matrix: List[list], index1: int, index2: int, start: int, stop: int):
    """ swap two rows in array """
    tmp = matrix[index1][start:stop].copy()
    matrix[index1][start:stop] = matrix[index2][start:stop]
    matrix[index2][start:stop] = tmp


# ---------------
# VECTORS METHODS
# ---------------

def sub_vectors(v1: list, v2: list):
    """ return vector which is subtract of 2 vectors """
    result = [0 for i in range(len(v1))]
    for i in range(len(v1)):
        result[i] = v1[i] - v2[i]
    return result


def multiply_vector_by_scalar(vector: list, scalar: float or int):
    """ return vector multiplyed by scalar """
    return [n*scalar for i, n in enumerate(vector)]


# ----------------
# MATRICES METHODS
# ----------------

def ones(n: int):
    """ return matrix NxN with ones in diagonal """
    matrix = []
    row = [0 for i in range(n)]
    for i in range(n):
        row[i] = 1
        matrix.append(row.copy())
        row[i] = 0
    return matrix


def eye(n: int):
    """ return matrix with ones on diagonal """
    matrix = [[0 for i in range(n)].copy() for i in range(n)]
    for i in range(n):
        matrix[i][i] = 1
    return matrix


def multiply_matrix_by_vector(matrix: List[list], vector: list):
    """ return vector which is result of multiplying matrix by vector """
    result = []

    for i in range(len(matrix[0])):
        sum = 0
        for j in range(len(matrix)):
            sum += vector[j] * matrix[i][j]
        result.append(sum)

    return result