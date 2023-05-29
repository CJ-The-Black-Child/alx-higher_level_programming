#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(0, list_length):
        try:

            element_1 = my_list_1[i]
            element_2 = my_list_2[i]

            division_result = element_1 / element_2

        except TypeError:
            print("wrong type")
            result.append(0)
        except ZeroDivisionError:
            print("division by 0")
            result.append(0)
        except IndexError:
            print("out of range")
            result.append(0)
        finally:
            result.append(0)
    return result
