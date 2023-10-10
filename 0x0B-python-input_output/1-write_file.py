#!/usr/bin/python3
"""Defines function that writes to a file"""

def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8)
    and returns the number of characters written"""
    count_ = 0
    with open(filename, 'w', encoding='utf-8') as file_:
        return file_.write(text)
