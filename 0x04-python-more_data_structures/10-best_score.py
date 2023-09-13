#!/usr/bin/python3

def best_score(a_dictionary):
    """Returns a key with the biggest integer value."""
    if a_dictionary:
        max_score = max(list(a_dictionary.values()))
        for key, score in a_dictionary.items():
            if score == max_score:
                return key
    return None
