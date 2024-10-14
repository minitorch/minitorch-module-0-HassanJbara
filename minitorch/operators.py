"""Collection of the core mathematical operators used throughout the code base."""

import math

# ## Task 0.1
from typing import Callable, List, Iterable

#
# Implementation of a prelude of elementary functions.

# Mathematical functions:
# - mul
# - id
# - add
# - neg
# - lt
# - eq
# - max
# - is_close
# - sigmoid
# - relu
# - log
# - exp
# - log_back
# - inv
# - inv_back
# - relu_back
#
# For sigmoid calculate as:
# $f(x) =  \frac{1.0}{(1.0 + e^{-x})}$ if x >=0 else $\frac{e^x}{(1.0 + e^{x})}$
# For is_close:
# $f(x) = |x - y| < 1e-2$


# TODO: Implement for Task 0.1.


def mul(x: float, y: float) -> float:
    """f(x, y) = x * y"""
    return x * y


def id(x: float) -> float:
    """id(x) = x"""
    return x


def add(x: float, y: float) -> float:
    """add(x, y) = x + y"""
    return x + y


def neg(x: float) -> float:
    """neg(x) = -x"""
    return -x


def lt(x: float, y: float) -> bool:
    """lt(x, y) = x < y"""
    return x < y


def eq(x: float, y: float) -> bool:
    """eq(x, y) = x == y"""
    return x == y


def max(x: float, y: float) -> float:
    """max(x, y)"""
    if x > y:
        return x
    else:
        return y


def is_close(x: float, y: float) -> bool:
    """|x - y| < 1e-2"""
    return abs(x - y) < 1e-2


def sigmoid(x: float) -> float:
    """sigmoid(x) = 1 / (1 + e^-x)"""
    return 1.0 / (1.0 + exp(-x))


def relu(x: float) -> float:
    """relu(x)"""
    return 0 if x < 0 else x


def log(x: float) -> float:
    """log(x)"""
    return math.log(x)


def exp(x: float) -> float:
    """exp(x) = e^x"""
    return math.e**x


def log_back(x: float, y: float) -> float:
    """log_back(x, y) = y * (dx/dy ln(x))"""
    return y / x


def inv(x: float) -> float:
    """inv(x) = 1 / x"""
    return 1 / x


def inv_back(x: float, y: float) -> float:
    """inv_back(x, y) = y * (dx/dy inv(x))"""
    return -2 * y * (1 / pow(x, 2))


def relu_back(x: float, y: float) -> float:
    """relu_back(x, y) = y * (dx/dy relu(x))"""
    if x < 0:
        return 0
    else:
        return y


# ## Task 0.3

# Small practice library of elementary higher-order functions.

# Implement the following core functions
# - map
# - zipWith
# - reduce
#
# Use these to implement
# - negList : negate a list
# - addLists : add two lists together
# - sum: sum lists
# - prod: take the product of lists


# TODO: Implement for Task 0.3.


def map(x: Iterable, func: Callable) -> Iterable:
    result = []

    for item in x:
        result.append(func(item))

    return result


def zipWith(x: Iterable, y: Iterable, func: Callable) -> Iterable:
    return map(zip(x, y), func)


def reduce(x: Iterable[float], func: Callable) -> float:
    result = 0

    for item in x:
        result = func(result, item)

    return result


def negList(x: Iterable) -> Iterable:
    return map(x, neg)


def addLists(x: Iterable, y: Iterable) -> Iterable:
    return zipWith(x, y, lambda pair: add(pair[0], pair[1]))


def sum(x: Iterable) -> float:
    return reduce(x, add)


def prod(x: Iterable) -> float:
    return reduce(x, mul)
