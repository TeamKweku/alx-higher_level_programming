#!/usr/bin/python3
def roman_to_int(roman_string):
    """ function that converts a Roman numeral to an integer
        Args:
            roman_string: provided roman numeral

        Returns:
            value in integer form
    """
    if not isinstance(roman_string, str) or roman_string is None:
        return (0)
    roman_numerals = {
        "M": 1000,
        "D": 500,
        "C": 100,
        "L": 50,
        "X": 10,
        "V": 5,
        "I": 1,
    }
    if len(roman_string) == 1:
        return roman_numerals[roman_string]
    total = roman_numerals[roman_string[0]]

    for i in range(1, len(roman_string)):
        for key, value in roman_numerals.items():
            if key == roman_string[i]:
                if roman_numerals[key] <= roman_numerals[roman_string[i - 1]]:
                    total += value
                    break
                else:
                    x = 2 * roman_numerals[roman_string[i - 1]]
                    total = total + roman_numerals[key] - x
                    break
    return (total)
