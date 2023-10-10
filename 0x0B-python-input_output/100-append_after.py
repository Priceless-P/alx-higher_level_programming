#!/usr/bin/python3
"""Defines a text file insertion function."""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text to a file,
    after each line containing a specific string.
    Args:
        filename: The name of the file.
        search_string: The string to search for within the file.
        new_string: The string to insert.
    """
    new_text = ""
    with open(filename) as file:
        for line in file:
            new_text += line
            if search_string in line:
                new_text += new_string
    with open(filename, "w") as file_:
        file_.write(new_text)
