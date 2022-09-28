#!/usr/bin/python3

"""Prints a dictionary by ordered keys."""


def print_sorted_dictionary(a_dictionary):
    for keys in sorted(a_dictionary.keys()):
        print("{:s}: {}".format(keys, a_dictionary[keys]))
