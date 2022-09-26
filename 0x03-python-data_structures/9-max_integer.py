#!/usr/bin/python3

def max_integer(my_list=[]):
    """Finds the biggest integer of a list"""
    if len(my_list) == 0:
        return None
    biggest_int = my_list[0]
    for x in range(1, len(my_list)):
        if my_list[x] > biggest_int:
            biggest_int = my_list[x]
    return biggest_int
