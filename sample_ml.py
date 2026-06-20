"""
Simple linear regression implementation from scratch.
"""

import math


def mean(values):
    return sum(values) / len(values)


def variance(values):
    m = mean(values)
    return sum((x - m) ** 2 for x in values) / len(values)


def covariance(x_vals, y_vals):
    mx = mean(x_vals)
    my = mean(y_vals)
    return sum((x - mx) * (y - my) for x, y in zip(x_vals, y_vals)) / len(x_vals)


def linear_regression(x_vals, y_vals):
    if len(x_vals) != len(y_vals) or len(x_vals) == 0:
        raise ValueError("x and y must be non-empty and the same length")
    v = variance(x_vals)
    if v == 0:
        raise ValueError("x values must not all be identical")
    slope = covariance(x_vals, y_vals) / v
    intercept = mean(y_vals) - slope * mean(x_vals)
    return slope, intercept


def predict(x, slope, intercept):
    return slope * x + intercept


def r_squared(x_vals, y_vals, slope, intercept):
    y_mean = mean(y_vals)
    ss_tot = sum((y - y_mean) ** 2 for y in y_vals)
    ss_res = sum((y - predict(x, slope, intercept)) ** 2 for x, y in zip(x_vals, y_vals))
    if ss_tot == 0:
        return 1.0
    return 1 - ss_res / ss_tot


def rmse(x_vals, y_vals, slope, intercept):
    errors = [(y - predict(x, slope, intercept)) ** 2 for x, y in zip(x_vals, y_vals)]
    return math.sqrt(mean(errors))


if __name__ == "__main__":
    # Study hours vs exam scores
    hours = [1, 2, 3, 4, 5, 6, 7, 8]
    scores = [50, 55, 65, 70, 75, 80, 85, 95]

    slope, intercept = linear_regression(hours, scores)
    r2 = r_squared(hours, scores, slope, intercept)
    error = rmse(hours, scores, slope, intercept)

    print(f"Slope:     {slope:.4f}")
    print(f"Intercept: {intercept:.4f}")
    print(f"R²:        {r2:.4f}")
    print(f"RMSE:      {error:.4f}")

    for h in [5, 9, 10]:
        print(f"  {h}h study -> predicted score: {predict(h, slope, intercept):.1f}")
