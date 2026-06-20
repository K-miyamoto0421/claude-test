"""
Simple linear regression implementation from scratch.
"""

import math
from typing import List, Tuple


def mean(values: List[float]) -> float:
    """リストの平均値を返す。

    Args:
        values: 数値のリスト。空でないこと。

    Returns:
        平均値。

    Raises:
        ValueError: values が空の場合。
    """
    if not values:
        raise ValueError("values must not be empty")
    return sum(values) / len(values)


def variance(values: List[float]) -> float:
    """リストの分散（母分散）を返す。

    Args:
        values: 数値のリスト。

    Returns:
        分散値。
    """
    m = mean(values)
    return sum((x - m) ** 2 for x in values) / len(values)


def covariance(x_vals: List[float], y_vals: List[float]) -> float:
    """2つのリストの共分散を返す。

    Args:
        x_vals: 説明変数のリスト。
        y_vals: 目的変数のリスト。x_vals と同じ長さであること。

    Returns:
        共分散値。

    Raises:
        ValueError: リストの長さが異なる場合。
    """
    if len(x_vals) != len(y_vals):
        raise ValueError(
            f"x_vals and y_vals must have the same length, got {len(x_vals)} and {len(y_vals)}"
        )
    mx = mean(x_vals)
    my = mean(y_vals)
    return sum((x - mx) * (y - my) for x, y in zip(x_vals, y_vals)) / len(x_vals)


def linear_regression(x_vals: List[float], y_vals: List[float]) -> Tuple[float, float]:
    """単回帰分析を行い、傾きと切片を返す。

    Args:
        x_vals: 説明変数のリスト。空でなく、y_vals と同じ長さであること。
        y_vals: 目的変数のリスト。

    Returns:
        (slope, intercept) のタプル。

    Raises:
        ValueError: リストが空・長さが異なる・x が全て同一値の場合。
    """
    if len(x_vals) != len(y_vals) or len(x_vals) == 0:
        raise ValueError("x and y must be non-empty and the same length")
    v = variance(x_vals)
    if v == 0:
        raise ValueError("x values must not all be identical")
    slope = covariance(x_vals, y_vals) / v
    intercept = mean(y_vals) - slope * mean(x_vals)
    return slope, intercept


def predict(x: float, slope: float, intercept: float) -> float:
    """線形モデルで予測値を返す。

    Args:
        x: 説明変数の値。
        slope: 回帰係数（傾き）。
        intercept: 切片。

    Returns:
        予測値 slope * x + intercept。
    """
    return slope * x + intercept


def r_squared(x_vals: List[float], y_vals: List[float], slope: float, intercept: float) -> float:
    """決定係数 R² を返す。

    Args:
        x_vals: 説明変数のリスト。
        y_vals: 目的変数のリスト。
        slope: 回帰係数（傾き）。
        intercept: 切片。

    Returns:
        R² の値（0.0 〜 1.0）。y が全て同一の場合は 1.0 を返す。
    """
    y_mean = mean(y_vals)
    ss_tot = sum((y - y_mean) ** 2 for y in y_vals)
    ss_res = sum((y - predict(x, slope, intercept)) ** 2 for x, y in zip(x_vals, y_vals))
    if ss_tot == 0:
        return 1.0
    return 1 - ss_res / ss_tot


def rmse(x_vals: List[float], y_vals: List[float], slope: float, intercept: float) -> float:
    """平均二乗誤差の平方根（RMSE）を返す。

    Args:
        x_vals: 説明変数のリスト。
        y_vals: 目的変数のリスト。
        slope: 回帰係数（傾き）。
        intercept: 切片。

    Returns:
        RMSE の値。
    """
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
