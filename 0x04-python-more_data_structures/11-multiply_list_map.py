#!/usr/bin/python3


def multiple_list_map(my_list=[], number=0):
    return list(map(lambda x: multiply(x, number), my_list))

def multiply(x, number):
    return x * number
