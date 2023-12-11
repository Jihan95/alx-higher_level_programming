#!/usr/bin/python3
def roman_to_int(roman_string):
    if (roman_string is None or type(roman_string) is not str):
        return (0)
    roman_numerals = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
            }
    total = 0
    prev_value = 0
    for i in range(len(roman_string) - 1, -1, -1):
        current_value = roman_numerals[roman_string[i]]
        if (current_value < prev_value):
            total = total - current_value
        else:
            total = total + current_value
        prev_value = current_value
    return total
