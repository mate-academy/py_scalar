"""
Find scalar product of two vectors
"""

from typing import List


def scalar_product(list_a, list_b):
    """ Scalar product """
    scal_sum = 0

    if list_a:
        for i in range(len(list_a)):
            scal_sum += int(list_a[i] * list_b[i])

    return scal_sum
