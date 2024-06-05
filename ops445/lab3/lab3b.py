#!/usr/bin/env python3
'''Lab 3 Part 1 script - functions'''
# Author ID: [157545211]

def sum_numbers(number1, number2):
    # Make this function add number1 and number2 and return the value
    return number1 + number2

def subtract_numbers(number1, number2):
    # Make this function subtract number1 and number2 and return the value
    # Remember to make sure the function accepts 2 arguments
    return number1 - number2

def multiply_numbers(number1, number2):
    # Make this function multiply number1 and number2 and return the value
    # Remember to make sure the function accepts 2 arguments
    return number1 * number2

if __name__ == '__main__':
    print(sum_numbers(10, 5))
    print(subtract_numbers(10, 5))
    print(multiply_numbers(10, 5))




import lab3b

print(lab3b.sum_numbers(10, 5))          # Should print 15
print(lab3b.sum_numbers(25, 25))         # Should print 50
print(lab3b.subtract_numbers(10, 5))     # Should print 5
print(lab3b.subtract_numbers(5, 10))     # Should print -5
print(lab3b.multiply_numbers(10, 5))     # Should print 50
print(lab3b.multiply_numbers(10, 2))     # Should print 20

