#!/usr/bin/env python3

import sys

# Check if the number of arguments is correct
if len(sys.argv) != 3:  # Including sys.argv[0], there should be 3 arguments in total
    print(f"Usage: {sys.argv[0]} name age")
    sys.exit()

# Assign arguments to variables
name = sys.argv[1]
age = int(sys.argv[2])  # Convert age to an integer

# Print the output message
print(f"Hi {name}, you are {age} years old.")

