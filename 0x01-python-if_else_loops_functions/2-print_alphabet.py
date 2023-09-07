#!/usr/bin/python3
"""Prints the ASCII alphabet,
in lowercase, not followed by a new line except q and e"""
for i in range(97, 123):
    print("{}".format(chr(i)), sep="", end="")
