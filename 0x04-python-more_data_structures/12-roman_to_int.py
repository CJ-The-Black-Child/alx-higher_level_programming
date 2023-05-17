#!/usr/bin/python3


def roman_to_int(roman_string):
    if not isinstance(roman_string, str) pr roman_string is None:
        return 0

    roman_value = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    total = 0
    n = len(roman_string)

    for i in range(n):
        if i < n - 1 and roman_value[roman_string[i]] < roman_value[roman_string[i + 1]]:
            total -= roman_value[roman_string[i]]
        else:
            total += roman_value[roman_string[i]]

    return total
