#!/usr/bin/python3
"""
Defines a script that finds a peak
in a list of unsorted integers
"""

def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted integers"""
    if (list_of_integers) and (len(list_of_integers) > 0):
        size_of_list = len(list_of_integers)
        if size_of_list == 1:
            return list_of_integers[0]
        elif size_of_list == 2:
            return max(list_of_integers)

        mid = int(size_of_list/2)
        peak = list_of_integers[mid]
        if peak > list_of_integers[mid - 1] and peak > list_of_integers[mid + 1]:
            return peak
        elif peak < list_of_integers[mid - 1]:
            return find_peak(list_of_integers[:mid])
        else:
            return find_peak(list_of_integers[mid:])
    else:
        return None
