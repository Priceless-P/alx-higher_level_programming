#!/usr/bin/python3
"""
Defines a function that returns True if
the object is exactly an instance of
the specified class ; otherwise False.
"""


def is_same_class(obj, a_class):
    """returns True if the object is exactly an
    nstance of the specified class
    """
    if type(obj) is not a_class:
        return False
    return True
