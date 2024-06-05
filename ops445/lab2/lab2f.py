#!/usr/bin/env python3
# Author: [Vilaskumar Patel]
# Author ID: [157545211]
# Date Created: 2024/06/05

import sys

# Convert the first command-line argument to an integer
timer = int(sys.argv[1])

# While loop to count down from timer to 1
while timer > 0:
    print(timer)
    timer -= 1

# Print "blast off!" when the countdown is complete
print('blast off!')

