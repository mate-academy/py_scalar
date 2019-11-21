"""
scalar_product
"""
from typing import List


def scalar_product(list_a: List[float], list_b: List[float]) -> float:
    """

    :param list_a: [float]
    :param list_b: [float]
    :return: float scalar product
    """
    result = .0
    for i, item in enumerate(list_a):
        result += item * list_b[i]

    return result
