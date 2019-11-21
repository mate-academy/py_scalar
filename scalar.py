"""doc"""


def scalar_product(first, second):
    """scalar product"""

    prod = 0
    iteration = len(first) if len(first) <= len(second) else len(second)
    for ind in range(iteration):
        prod += first[ind] * second[ind]

    return prod
