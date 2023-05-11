#!/usr/bin/python3
import dis


def magic_calculation(a, b):
    from magic_calculation_102 import add, sub

    c = 0
    for i in range(4, 6):
        c = add(c, i)
        return sub(a, b) if a < b else c
    print(dis.dis(magic_calculation))
