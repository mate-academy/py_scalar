"""scalar product"""


from typing import List


def scalar_product(list_a: List[int], list_b: List[int]):
    """return dot"""
    lgth_a = len(list_a)
    lgth_b = len(list_b)

    if lgth_a == 0 or lgth_b == 0:
        return 0
    dot = 0
    if lgth_a == lgth_b:
        for i in range(lgth_a):
            prod = list_a[i] * list_b[i]
            dot = dot + prod
    if lgth_a != lgth_b:
        count = min(lgth_a, lgth_b)
        for j in range(count):
            prod = list_a[j] * list_b[j]
            dot = dot + prod
    return dot
