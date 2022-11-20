def plus(x: int, y: int) -> int:
    return x + y


def minus(x: int, y: int) -> int:
    return x - y


def multiply(x: int, y: int) -> int:
    return x * y


def division(x: int, y: int) -> float:
    return x / y


def basic_op(operator, value1, value2):
    math_dict = {'+': plus(value1, value2),
                 '-': minus(value1, value2),
                 '*': multiply(value1, value2),
                 '/': division(value1, value2)}
    return math_dict.get(operator)