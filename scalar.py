"""scalar vector product module"""
from typing import List


def scalar_product(first_vector: List[int], second_vector: List[int]) -> int:
    """scalar vector product function"""
    lenght_first, lenght_seond = len(first_vector), len(second_vector)
    if lenght_first == 0 or lenght_seond == 0:
        return 0
    if lenght_first < lenght_seond:
        count = lenght_first
    else:
        count = lenght_seond
    result = 0
    for index in range(count):
        result += first_vector[index] * second_vector[index]
    return result
