#!/usr/bin/env python3
#Author: Vilaskumar Patel
#Course: OPS445
#Prof.: Leo Lu
"""
This script asks the user if they like certain cafeteria foods.
"""

# Step 2: Create an immutable iterable
cafeteria_food = ("pizza", "salad", "sandwich", "soup")

# Step 3: For each item in cafeteria_food, ask the user if they like it or not
for food in cafeteria_food:
    answer = input(f"Do you like {food}? (yes/no): ")
    # No need to save the user's answers

