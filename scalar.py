"""Scalar module"""
from typing import List


def scalar_product(a_vect: List[int], b_vect: List[int]) -> int:
    """:returns scalar product of two vectors"""
    result = 0
    for a_i, b_i in zip(a_vect, b_vect):
        result += a_i*b_i
    return result
