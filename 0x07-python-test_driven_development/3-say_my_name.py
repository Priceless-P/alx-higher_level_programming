#!/usr/bin/bash
"""Prints My name is <first name> <last name>
"""


def say_my_name(first_name, last_name=""):
    """Prints a formatted name string.
        Args:
            first_name (str): The first name to be included
            in the formatted string.
            last_name (str, optional): The last name to be
            included in the formatted string.
            Defaults to an empty string.
        Returns:
            None
        Raises:
            TypeError: If first_name or last_name is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
