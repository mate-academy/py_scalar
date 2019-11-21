"""Docstring"""

def scalar_product(vec_1, vec_2):
    """Returns a scalar product of vec_1 and vec_2"""
    s_product = 0
    for idx, elem in enumerate(vec_2):
        try:
            s_product += elem * vec_1[idx]
        except IndexError:
            return s_product

    return s_product
