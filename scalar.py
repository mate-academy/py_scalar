"""Calculating scalar product
of two vectors
"""

from itertools import zip_longest


def scalar_product(first_vector,
                   second_vector):
    """General function"""
    result = 0
    if not first_vector or not second_vector:
        return result
    result = sum([a*b for a, b in zip_longest(first_vector, second_vector, fillvalue=0)])
    return result
