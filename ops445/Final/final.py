#!/usr/bin/env python3
"""
Author: [Your Name]
"""

import sys
import os

# Define empty lists outside the main block
user_input = []
file_output = []

def testdir_files():
    """List the contents of the testdir directory and return as a list of files."""
    return os.listdir('testdir')

def letter_check(s):
    """Check if the string contains 'd', 'e', or 'f' and return True/False."""
    return any(char in s for char in 'def')

def main():
    global user_input
    global file_output

    # Get user input using command line arguments
    user_input = sys.argv[1:]

    if not user_input:
        print("No args found!")
        return

    # Call the function to get files from testdir
    file_output = testdir_files()

    # Add file_output to the end of user_input
    user_input.extend(file_output)

    # Loop through each item in the list and check with letter_check function
    for filename in user_input:
        if letter_check(filename):
            print(f"{filename}: Yes !!")
        else:
            print(f"{filename}: No !!")

    # Write items that returned True to a new file called output
    with open('output', 'w') as f:
        for item in user_input:
            if letter_check(item):
                f.write(item + '\n')

    # Print content of the 'output' file
    print("\nContent of 'output' file:")
    with open('output', 'r') as f:
        print(f.read())

if __name__ == "__main__":
    main()

