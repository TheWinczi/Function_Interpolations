from typing import List
from sys import maxsize


def calculate_error(values: List[float], interpolated: List[int]):
    """ calculate error and return types of errors as dictionary """

    errors = {
        "max": 0,
        "min": float(maxsize),
        "avg": 0.0,
        "avgs": [],
        "sum": 0.0,
        "sums": [],
        "errors": []
    }

    for i, value in enumerate(values):
        diff = float(abs(value - interpolated[i]))

        if diff > errors["max"]:
            errors["max"] = diff

        if diff < errors["min"]:
            errors["min"] = diff

        errors["sum"] += diff
        errors["sums"].append(errors["sum"])
        errors["avgs"].append(errors["sum"] / (i+1))
        errors["errors"].append(diff)

    errors["avg"] = errors["sum"] / len(values)
    return errors



