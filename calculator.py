"""Simple calculator module."""

from typing import Union

Number = Union[int, float]


def add(a: Number, b: Number) -> Number:
    """2つの数値を加算する。

    Args:
        a: 1つ目の数値。
        b: 2つ目の数値。

    Returns:
        a + b の結果。

    Raises:
        TypeError: a または b が数値でない場合。
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError(f"Operands must be numeric, got {type(a).__name__} and {type(b).__name__}")
    return a + b


def subtract(a: Number, b: Number) -> Number:
    """2つの数値を減算する。

    Args:
        a: 被減数。
        b: 減数。

    Returns:
        a - b の結果。

    Raises:
        TypeError: a または b が数値でない場合。
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError(f"Operands must be numeric, got {type(a).__name__} and {type(b).__name__}")
    return a - b


def multiply(a: Number, b: Number) -> Number:
    """2つの数値を乗算する。

    Args:
        a: 1つ目の数値。
        b: 2つ目の数値。

    Returns:
        a * b の結果。

    Raises:
        TypeError: a または b が数値でない場合。
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError(f"Operands must be numeric, got {type(a).__name__} and {type(b).__name__}")
    return a * b


def divide(a: Number, b: Number) -> float:
    """2つの数値を除算する。

    Args:
        a: 被除数。
        b: 除数。

    Returns:
        a / b の結果。

    Raises:
        TypeError: a または b が数値でない場合。
        ValueError: b がゼロの場合。
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError(f"Operands must be numeric, got {type(a).__name__} and {type(b).__name__}")
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def calculate(a: Number, operator: str, b: Number) -> Number:
    """演算子文字列を使って2つの数値を計算する。

    Args:
        a: 1つ目の数値。
        operator: 演算子（'+', '-', '*', '/'）。
        b: 2つ目の数値。

    Returns:
        演算結果。

    Raises:
        TypeError: a または b が数値でない場合。
        ValueError: 未知の演算子が指定された場合。
    """
    ops = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
    }
    if operator not in ops:
        raise ValueError(f"Unknown operator: {operator!r}. Must be one of {list(ops.keys())}")
    return ops[operator](a, b)


if __name__ == "__main__":
    examples = [
        (10, "+", 5),
        (10, "-", 3),
        (4, "*", 7),
        (20, "/", 4),
    ]
    for a, op, b in examples:
        print(f"{a} {op} {b} = {calculate(a, op, b)}")
