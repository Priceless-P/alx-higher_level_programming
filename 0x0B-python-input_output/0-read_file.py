#!/usr/bin/python3
"""Defines a text file-reading function."""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout"""
    with open(filename, 'r') as contents:
        for line in contents:
            print("{}".format(line), end="")
