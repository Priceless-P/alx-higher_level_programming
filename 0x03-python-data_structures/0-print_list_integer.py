#!/usr/bin/python3

def print_list_integer(my_list=[]):
    """Prints all integers of a list."""
    for i, _ in enumerate(my_list):
        print("{:d}".format(my_list[i]))
