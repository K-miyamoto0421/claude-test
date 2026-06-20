"""Simple calculator module."""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def calculate(a, operator, b):
    ops = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
    }
    if operator not in ops:
        raise ValueError(f"Unknown operator: {operator}")
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
