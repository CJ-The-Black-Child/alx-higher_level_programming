#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            element_1 = my_list_1[i]
            element_2 = my_list_2[i]

            if not isinstance(element_1, (int, float)) or \
                    not isinstance(element_2, (int, float)):
                raise TypeError("wrong type")

            division_result = element_1 / element_2

            result.append(division_result)
        except ZeroDivisionError:
            result.apped(0)
            print("division by 0")
        except IndexError:
            result.append(0)
            print("out of range")
    return result
