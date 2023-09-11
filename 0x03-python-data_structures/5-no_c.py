#!/usr/bin/python3
def no_c(my_string):
    """Removes all characters c and C from a string"""
    result = ""
    for i in my_string:
        if (i == 'c') or (i == 'C'):
            continue
        result += i
    return result
