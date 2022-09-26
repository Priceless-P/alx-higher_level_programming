#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """Prints all integers of a list, in reverse order."""
    if isinstance(my_list, list):
        my_list.reverse()
        for x in range(len(my_list)):
            print("{}".format(my_list[x]))
