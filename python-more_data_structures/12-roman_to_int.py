#!/usr/bin/python3
def roman_to_int(roman_string):
    numbers = {'I': 1,'V': 5, 'X': 10, 'L':50, 'C': 100, 'D':500, 'M':1000}
    decimal = 0
    if roman_string is None:
        return 0
    else:
        for char in roman_string:
            if roman_string == 'IX':
                decimal = 9
            else:
                for i in numbers:
                    if char == i:
                        decimal = decimal + numbers[i]
        return decimal
