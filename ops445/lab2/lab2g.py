#!/usr/bin/env python3
# Author: [Vilaskumar Patel]
# Author ID: [157545211]
# Date Created: 2024/06/05

import sys

# Check if a command line argument is provided
if len(sys.argv) > 1:
    timer = int(sys.argv[1])  # Convert the argument to an integer
else:
    timer = 3  # Default timer value if no argument is provided

# While loop to count down from timer to 1
while timer > 0:
    print(timer)
    timer -= 1

# Print "blast off!" when the countdown is complete
print('blast off!')

