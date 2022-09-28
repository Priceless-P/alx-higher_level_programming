#!/usr/bin/python3

"""Converts a Roman numeral to an integer."""


def roman_to_int(roman_string):
    roman_def = {
        'I':1,
        'V': 5,
        'X': 10,
        'L':50,
        'C': 100,
        'D': 500,
        'M':100
    }
    num = 0;
    for x in range(len(roman_string)):
        if roman_def.get(roman_string[x], 0) == 0:
            return  0
        if (x != len(roman_string) - 1) and roman_def[roman_string[x]] < roman_string[x + 1]:
            num += roman_def[roman_string[x]] * - 1
        else:
            num += roman_def[roman_string[x]]
    return num