#!/usr/bin/python3
def max_integer(my_list=[]):
    """Finds the biggest integer of a list."""
    if len(my_list) != 0:
        max_num = 0
        for i, _ in enumerate(my_list):
            if my_list[i] > max_num:
                max_num = my_list[i]
        return max_num
    else:
        return None
