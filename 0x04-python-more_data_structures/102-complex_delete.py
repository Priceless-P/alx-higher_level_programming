#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    """Deletes keys with a specific value in a dictionary."""
    for key, val in a_dictionary.items():
        if val == value:
            del key
    return a_dictionary
