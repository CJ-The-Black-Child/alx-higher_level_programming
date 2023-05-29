#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """
    Divides element by element two lists and returns a new list with the
        division results.
    Args:
        my_list_1 (list): The first list.
        my_list_2 (list): The second list.
        list_length (int): The desired length of the resulting list.

    Returns:
        list: A new list with the division results.
    """
    result = []
    for i in range(0, list_length):
        try:
            element_1 = my_list_1[i]
            element_2 = my_list_2[i]
            division_result = element_1 / element_2
        except TypeError:
            print("wrong type")
            division_result = 0
        except ZeroDivisionError:
            print("division by 0")
            division_result = 0
        except IndexError:
            print("out of range")
            division_result = 0
        finally:
            result.append(division_result)
    return result
