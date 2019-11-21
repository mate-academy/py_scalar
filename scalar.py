"""
Find scalar product of two vectors
"""

from typing import List

def scalar_product(list_a: List[float], list_b: List[float]) -> int:
    """ Scalar product """
    scal_sum = 0

    if list_a:
        len_list = len(list_a)
        for i in range(len_list):
            scal_sum += int(list_a[i] * list_b[i])

    return scal_sum
