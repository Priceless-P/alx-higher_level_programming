#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    """Return a new dictionary with all values multipled by 2."""
    new_list = a_dictionary.copy()
    list_keys = list(new_list.keys())

    for x in list_keys:
        new_list[x] *= 2
    return new_list
