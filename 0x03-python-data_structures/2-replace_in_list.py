#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """Replaces an element of a list at a specific position"""
    if (idx >= 0) and (idx < len(my_list)):
        for x in range(len(my_list)):
            if x == idx:
                my_list[idx] = element
                return my_list
    else:
        return my_list
