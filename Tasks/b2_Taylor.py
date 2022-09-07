"""
Taylor series
"""
import math as m

from typing import Union

COUNT_SEQ = 20

def ex(x: Union[int, float]) -> float:
    """
    Calculate value of e^x with Taylor series

    :param x: x value
    :return: e^x value
    """
    print(x)

    gen = range(1, COUNT_SEQ)
    val = 1

    for idx in gen:
        val += x ** idx / m.factorial(idx)

    return val


def ex_mod(x: Union[int, float]) -> float:
    """
    Calculate value of e^x with Taylor series

    :param x: x value
    :return: e^x value
    """
    print(x)

    gen = range(1, COUNT_SEQ)
    val = 1
    fact = 1
    pow_ = 1

    for idx in gen:
        fact *= idx
        pow_ *= x
        val += pow_ / fact

    return val

def sinx(x: Union[int, float]) -> float:
    """
    Calculate sin(x) with Taylor series

    :param x: x value
    :return: sin(x) value
    """
    print(x)

    gen = range(1, COUNT_SEQ)
    val = x

    for idx in gen:
        sign = (-1) ** idx
        val += sign * x ** (2 * idx + 1) / m.factorial(2 * idx + 1)

    return val


def sinx_mod(x: Union[int, float]) -> float:
    """
    Calculate sin(x) with Taylor series

    :param x: x value
    :return: sin(x) value
    """
    print(x)

    gen = range(1, COUNT_SEQ)
    val = x
    fact = 6
    pow_ = x ** 3
    sign = -1

    for idx in gen:
        val += sign * pow_ / fact
        sign *= -1
        pow_ *= x ** 2
        fact *= 4 * idx ** 2 + 10 * idx + 6  # (2 * idx + 2) * (2 * idx + 3)

    return val
