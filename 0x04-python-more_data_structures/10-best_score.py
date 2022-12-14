#!/usr/bin/python3
"""Returns a key with the biggest integer value"""


def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None
    new_dic = list(a_dictionary.keys())[0]
    biggest = a_dictionary[new_dic]
    for key, value in a_dictionary.items():
        if value > biggest:
            biggest = value
            new_dic = key
    return new_dic
