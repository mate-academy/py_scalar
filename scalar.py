"""module docstring"""
#from typing import List

def scalar_product(first_list, second_list):
    """docstring"""
    if first_list == [] or second_list == []:
        result = 0
    else:
        result = 0
        if len(first_list) <= len(second_list):
            min_lenth = len(first_list)
        else:
            min_lenth = len(second_list)
        for number in range(min_lenth):
            result += first_list[number] * second_list[number]
        print(result)
    return result
