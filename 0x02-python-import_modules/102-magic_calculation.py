#!/usr/bin/python3
from magic_calculation_102 import add, sub

def magic_calculation(a, b):
    c = 0
    for i in range(4, 6):
        c = add(c, i)
        return sub(a, b) if a < b else c
