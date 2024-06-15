#!/usr/bin/env python3
# Author ID: [vpatel255-157545211]

def is_digits(sobj):
    # This function checks if all characters in sobj are digits
    for char in sobj:
        if not char.isdigit():
            return False
    return True

if __name__ == '__main__':
    test_list = ['x3058', '3058', '8503x', '8503']
    for item in test_list:
        if is_digits(item):
            print(item, 'is an integer.')
        else:
            print(item, 'is not an integer.')


import lab4e

print(lab4e.is_digits('65'))  # Will output True
print(lab4e.is_digits('1F'))  # Will output False
print(lab4e.is_digits('-12'))  # Will output False

