#!/usr/bin/python3


def roman_to_int(roman_string):
    result = 0

    if (not isinstance(roman_string, str)) or (not roman_string):
        return result

    t = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
    for unit in roman_string:
        result += t[unit]

    for x in ["CD", "CM", "XL", "XC", "IV", "IX"]:
        if x in roman_string:
            result -= 2 * t[x[0]]

    return result
