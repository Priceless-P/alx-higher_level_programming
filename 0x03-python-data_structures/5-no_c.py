#!/usr/bin/env python3

def no_c(my_string):
    """Removes all characters c and C from a string."""
    str_copy = my_string.translate({ord(x): None for x in 'cC'})
    return str_copy
