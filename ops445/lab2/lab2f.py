#!/usr/bin/env python3
# Author: [Your Full Name]
# Author ID: [Your Seneca ID]
# Date Created: yyyy/mm/dd

import sys

# Convert the first command-line argument to an integer
timer = int(sys.argv[1])

# While loop to count down from timer to 1
while timer > 0:
    print(timer)
    timer -= 1

# Print "blast off!" when the countdown is complete
print('blast off!')

