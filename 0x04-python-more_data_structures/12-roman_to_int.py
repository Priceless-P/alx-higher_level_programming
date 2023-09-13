#!/usr/bin/python3

def roman_to_int(roman_string):
    """Converts a Roman numeral to an integer."""
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    # Check if the input is a valid string or None
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    result = 0
    prev_value = 0

    # Iterate through the Roman string from right to left
    for char in reversed(roman_string):
        value = roman_values.get(char, 0)

        # If the current value is less than the previous value, subtract it
        if value < prev_value:
            result -= value
        else:
            result += value
        prev_value = value
    return result
