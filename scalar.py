"""
scalar product module
"""

from typing import List


def scalar_product(frst_vector: List[float], sec_vector: List[float]) -> float:
    """
    Scalar product of two vectors.
    :param frst_vector: List[float]
    :param sec_vector: List[float]
    :return: int
    """
    if len(frst_vector) == len(sec_vector):
        scalar_prd = sum([frst_vector[idx] * sec_vector[idx] for idx in range(len(sec_vector))])
    elif len(frst_vector) < len(sec_vector):
        scalar_prd = sum([frst_vector[idx] * sec_vector[idx] for idx in range(len(frst_vector))])
    else:
        return 0
    return scalar_prd


def scalar_product_den_solution(frst_vector: List[float], sec_vector: List[float]) -> float:
    sum_result = 0
    for el1, el2 in zip(frst_vector, sec_vector):
        sum_result += el1 * el2
    return sum_result
