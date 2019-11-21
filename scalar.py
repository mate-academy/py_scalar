'''
Module
'''
from typing import List


def scalar_product(list_a: List[int], list_b: List[int]) -> int:
    '''

    :param list_a:
    :param list_b:
    :return:
    '''
    result = 0
    for elem_a, elem_b in zip(list_a, list_b):
        result += elem_a * elem_b
    return result
