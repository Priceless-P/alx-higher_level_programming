#!/usr/bin/python3

def multiple_returns(sentence):
    """Returns a tuple with the length of a string and its first character"""

    if len(sentence) == 0:
        first_character = None
        tuple_length = 0
    else:
        sentence = list(sentence)
        tuple_length = len(sentence)
        new = str(sentence[0])
        first_character = new[0]
    return tuple_length, first_character
