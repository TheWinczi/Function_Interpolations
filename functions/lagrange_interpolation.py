from typing import List


def lagrange_interpolation(xs: List[float], ys: List[float], arguments: List[float]):
    """ interpolate function using input data using
        polynomial Lagrange method """
    values = []

    for x in arguments:
        value = 0.0
        for i in range(len(xs)):
            t = 1.0
            for j in range(len(xs)):
                if i != j:
                    t = t * ((x - xs[j]) / (xs[i] - xs[j]))

            value += t * ys[i]
        values.append(value)

    return values
