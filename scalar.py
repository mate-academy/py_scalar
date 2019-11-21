"""
docstring
"""
import numpy as np


def scalar_product(list_one, list_two):
    """

    :param list_one:
    :param list_two:
    :return:
    """
    longer_list, shorter_list = max(list_one, list_two), min(list_one, list_two)
    if len(longer_list) != len(shorter_list):
        for _ in range(len(longer_list)-len(shorter_list)):
            shorter_list.append(0)

    return np.dot(longer_list, shorter_list)
