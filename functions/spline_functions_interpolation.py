from typing import List

from functions import lu_factorization as lu


def spline_functions_interpolation(xs: List[float], ys: List[float], arguments: List[float]):
    """ interpolate function using input data using
        spline functions method """

    nodes_number = len(xs)
    coeffs_number = (nodes_number - 1) * 4

    values, coefficients = [], []
    b_vector = [0.0 for i in range(coeffs_number)]
    a_matrix = [[0.0 for i in range(coeffs_number)].copy() for i in range(coeffs_number)]

    for i in range(nodes_number - 1):
        x0 = xs[i]
        x1 = xs[i+1]
        h = x1 - x0

        a_matrix[4*i][4*i] = 1
        b_vector[4*i] = ys[i]

        a_matrix[4*i+1][4*i:4*i+4] = [1, h, h**2, h**3]
        b_vector[4*i+1] = ys[i+1]

        if i >= 1:
            a_matrix[4*i+2][4*(i-1)+1:4*(i-1)+4] = [1, 2*h, 3*h**2]
            a_matrix[4*i+2][4*i+1] = -1

            a_matrix[4*i+3][4*(i-1) + 2] = 2
            a_matrix[4*i+3][4*(i-1) + 3] = 6 * h
            a_matrix[4*i+3][4*i+2] = -2
        else:
            a_matrix[2][2] = 2

            h = xs[nodes_number - 1] - xs[nodes_number - 2]
            a_matrix[3][4 * (nodes_number - 1) - 3] = 2
            a_matrix[3][4 * (nodes_number - 1) - 2] = 6 * h

    # calculate coefficients using LU factorization(decomposition)
    coefficients = lu.lu_factorization(a_matrix, b_vector)

    # calculate interpolated function value for all arguments
    args_index = 0
    for i in range(nodes_number-1):
        x0 = xs[i]
        x1 = xs[i+1]
        while args_index < len(arguments):
            arg = arguments[args_index]
            if arg > x1:
                break
            values.append(get_value(x0, arg, coefficients[i*4:(i+1)*4]))
            args_index += 1
        if args_index >= len(arguments):
            break

    return values


def get_value(x0: float, x: float, coefficients: List[float]):
    """ calculate value in interval [x0, x1] where function has defined coefficients """
    sum = coefficients[0]
    for i in range(1, len(coefficients)):
        sum += (x - x0) ** i * coefficients[i]

    return sum
