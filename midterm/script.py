#!/usr/bin/env python3
"""
Author: Vilaskumar Patel
Id: vpatel255
Course: OPS445
"""

def main():
    total = 0
    count = 0

    while True:
        user_input = input("Enter a number (or press Enter to finish): ")
        
        if user_input == "":
            break
        
        if user_input.isnumeric():
            total += int(user_input)
            count += 1
        else:
            print(f"'{user_input}' is not a valid number. Ignoring it.")

    if count > 0:
        average = total / count
        print(f"The average of the entered numbers is: {average}")
    else:
        print("No valid numbers were entered.")

if __name__ == "__main__":
    main()

