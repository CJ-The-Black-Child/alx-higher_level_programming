#!/usr/bin/python3
def divisible_by_2(my_list=None):
    if my_list is None:
        return []
    result = []
    for num in my_list:
        result.append(num % 2 == 0)

    return result
