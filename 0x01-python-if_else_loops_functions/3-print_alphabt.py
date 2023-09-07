#!/usr/bin/python3
"""Prints the ASCII alphabet,
in lowercase, not followed by a new line"""
for i in range(97, 123):
    if i == 101 or i == 113:
        continue
    print("{}".format(chr(i)), sep="", end="")
