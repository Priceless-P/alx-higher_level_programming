#!/usr/bin/python3

def weight_average(my_list=[]):
    """Returns the weighted average of all
    integers tuple (<score>, <weight>)"""
    if not isinstance(my_list, list) or len(my_list) == 0:
        return 0

    total_score = 0
    total_weight = 0
    for scores in my_list:
        total_score += scores[0] * scores[1]
        total_weight += scores[1]
    return total_score / total_weight
