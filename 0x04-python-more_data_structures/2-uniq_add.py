#!/usr/bin/python3

"""Adds all unique integers in a list (only once for each integer"""


def uniq_add(my_list=[]):
    new_list = 0
    for x in set(my_list):
        new_list += x
    return new_list
