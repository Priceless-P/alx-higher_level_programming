#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """Replaces an element in a list at a specific position without
    modifying the original list (like in C)."""
    if (idx >= 0) and (idx < len(my_list)):
        new_list = my_list.copy()
        for i in range(len(my_list)):
            if i == idx:
                new_list[idx] = element
                return new_list
    else:
        return my_list
