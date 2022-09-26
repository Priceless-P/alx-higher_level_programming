#!/usr/bin/env python3

def no_c(my_string):
    """Removes all characters c and C from a string."""
    str_copy = ""
    for x in my_string:
        if x == "c" or x == "C":
            continue
        else:
            str_copy += 1
    return str_copy
