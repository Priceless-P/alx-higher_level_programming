#!/usr/bin/python3

"""Prints a dictionary by ordered keys."""


def print_sorted_dictionary(a_dictionary):
    [print("{}:{}".format(key, value)) for key, value in sorted(a_dictionary.items())]
