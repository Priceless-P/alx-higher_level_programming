#!/usr/bin/python3

def multiple_returns(sentence):
    """Returns a tuple with the length of a string and its first character"""

    tuple_length = len(sentence);
    first_character = sentence[0];

    return tuple_length, first_character
