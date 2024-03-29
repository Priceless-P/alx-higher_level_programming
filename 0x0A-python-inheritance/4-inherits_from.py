#!/usr/bin/python3
"""
Defines a function that returns True
if the object is an instance of a class
that inherited (directly or indirectly) from
the specified class ; otherwise False.
"""


def inherits_from(obj, a_class):
    """Checks if an object is an inherited instance of a class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        If obj is an inherited instance of a_class - True.
        Otherwise - False.
    """

    if not issubclass(type(obj), a_class) and type(obj) is not a_class:
        return False
    return True
