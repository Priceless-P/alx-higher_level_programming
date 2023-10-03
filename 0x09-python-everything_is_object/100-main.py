#!/usr/bin/python3
magic_string = __import__('100-magic_string').magic_string

for i in range(10):
    magic_string.n = getattr(magic_string, 'n', 0) + 1
    print(magic_string())
