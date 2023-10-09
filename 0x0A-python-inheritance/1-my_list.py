#!/usr/bin/python3
"""
Defines a class MyList that inherits from list with
in  instance method: def print_sorted(self): that prints
the list, but sorted (ascending sort)
"""


class MyList(list):
    """Implements sorted printing for the built-in list class."""

    def print_sorted(self):
        """Print a list in sorted ascending order."""
        print(sorted(self))
