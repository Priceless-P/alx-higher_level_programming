#!/usr/bin/python3
"""Prints numbers from 0 to 99"""
for i in range(0, 100):
    if i < 99:
        print("{}{}".format(0, i) if i < 10 else "{}".format(i), end=", ")
    else:
        print("{}".format(i))