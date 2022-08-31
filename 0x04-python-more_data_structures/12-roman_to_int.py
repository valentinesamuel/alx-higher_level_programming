#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    total = 0
    r = {'M': 1000,
         'D': 500,
         'C': 100,
         'L': 50,
         'X': 10,
         'V': 5,
         'I': 1}
    for i in range(len(roman_string), 0, -1):
        if roman_string[i-1] in r:
            total = total + r[roman_string[i-1]]
            if i != 0 and (i-2) >= 0:
                if r[roman_string[i - 2]] < r[roman_string[i - 1]]:
                    total = total - (2 * r[roman_string[i - 2]])
        else:
            return 0
    return total
