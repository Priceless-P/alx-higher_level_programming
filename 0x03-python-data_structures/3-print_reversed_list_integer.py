#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """Prints all integers of a list, in reverse order."""
    my_list = reversed(my_list)
    for i in my_list:
        print("{}".format(my_list[i]))
