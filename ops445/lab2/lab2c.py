#!/usr/bin/env python3

import sys

# Ensure we have enough arguments
if len(sys.argv) != 3:
    print("Usage: ./lab2c.py <name> <age>")
    sys.exit(1)

name = sys.argv[1]
age = int(sys.argv[2])

print('Hi ' + name + ', you are ' + str(age) + ' years old.')

