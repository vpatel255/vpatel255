#!/usr/bin/env python3

"""
Author: Vilaskumar Patel
Author ID: vpatel255
Course: OPS445
"""

def capital_vowel(target: str) -> bool:
    """
    Returns True if the string contains any of the uppercase vowels A, E, I, O, U
    """
    vowels = "AEIOU"
    for char in target:
        if char in vowels:
            return True
    return False

if __name__ == "__main__":
    test_string = input("Enter a string: ")
    if capital_vowel(test_string):
        print("The string contains an uppercase vowel.")
    else:
        print("The string does not contain any uppercase vowels.")

