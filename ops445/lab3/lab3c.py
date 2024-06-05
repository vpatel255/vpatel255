#!/usr/bin/env python3
'''Lab 3 Inv 2 function operate '''
# Author ID: [157545211]

def operate(number1, number2, operator):
    if operator == 'add':
        result = number1 + number2
    elif operator == 'subtract':
        result = number1 - number2
    elif operator == 'multiply':
        result = number1 * number2
    else:
        result = 'Error: function operator can be "add", "subtract", or "multiply"'
    return result

if __name__ == '__main__':
    print(operate(10, 5, 'add'))        # Expected output: 15
    print(operate(10, 5, 'subtract'))   # Expected output: 5
    print(operate(10, 5, 'multiply'))   # Expected output: 50
    print(operate(10, 5, 'divide'))     # Expected output: Error message



import lab3c

print(lab3c.operate(10, 20, 'add'))          # Should return 30
print(lab3c.operate(2, 3, 'add'))            # Should return 5
print(lab3c.operate(100, 5, 'subtract'))     # Should return 95
print(lab3c.operate(10, 20, 'subtract'))     # Should return -10
print(lab3c.operate(5, 5, 'multiply'))       # Should return 25 (Note: This is corrected to 25 instead of 50 as in your provided example.)
print(lab3c.operate(10, 100, 'multiply'))    # Should return 1000
print(lab3c.operate(100, 5, 'divide'))       # Should return error message
print(lab3c.operate(100, 5, 'power'))        # Should return error message

