#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    """Deletes keys with a specific value in a dictionary."""
    for key in list(a_dictionary.keys()):
        if value == a_dictionary.get(key):
            del a_dictionary[key]
    return a_dictionary
