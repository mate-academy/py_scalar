"""
docstring
"""


def scalar_product(list_one, list_two):
    """

    :param list_one:
    :param list_two:
    :return:
    """
    product = 0
    longer_list, shorter_list = max(list_one, list_two), min(list_one, list_two)
    for index, item in enumerate(shorter_list):
        product += longer_list[index] * item
    return product
