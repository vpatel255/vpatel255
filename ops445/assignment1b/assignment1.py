#!/usr/bin/env python3

'''
OPS445 Assignment 1 - Fall 2023
Program: assignment1.py
The python code in this file is original work written by
"Vilaskumar Patel". No code in this file is copied from any other source
except those provided by the course instructor, including any person,
textbook, or on-line resource. I have not shared this python script
with anyone or anything except for submission for grading. I understand
that the Academic Honesty Policy will be enforced and
violators will be reported and appropriate action will be taken.

Author: Vilaskumar Patel
Description : ID:- vpatel255
'''

import sys

def day_of_week(date: str) -> str:
    "Based on the algorithm by Tomohiko Sakamoto"
    year, month, day = (int(x) for x in date.split('-'))
    days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    offset = {1:0, 2:3, 3:2, 4:5, 5:0, 6:3, 7:5, 8:1, 9:4, 10:6, 11:2, 12:4}
    if month < 3:
        year -= 1
    num = (year + year//4 - year//100 + year//400 + offset[month] + day) % 7
    return days[num]

def leap_year(year: int) -> bool:
    "Return True if the year is a leap year"
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def mon_max(month: int, year: int) -> int:
    "Returns the maximum day for a given month. Includes leap year check"
    mon_dict = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
                7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    if month == 2 and leap_year(year):
        return 29
    return mon_dict.get(month, 31)  # Default to 31 if month not found

def after(date: str) -> str:
    '''
    after() -> date for next day in YYYY-MM-DD string format

    Return the date for the next day of the given date in YYYY-MM-DD format.
    This function has been tested to work for year after 1582
    '''
    # Detect date format
    if '-' in date:
        year, month, day = (int(x) for x in date.split('-'))
    elif '/' in date:
        day, month, year = (int(x) for x in date.split('/'))
    else:
        raise ValueError("Invalid date format. Use YYYY-MM-DD or DD/MM/YYYY.")

    day += 1  # next day

    if month == 2 and leap_year(year):
        mon_max_days = 29
    else:
        mon_dict = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
                    7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        mon_max_days = mon_dict[month]

    if day > mon_max_days:
        month += 1
        if month > 12:
            year += 1
            month = 1
        day = 1  # if day > this month's max, reset to 1

    # Return date in the same format as input
    if '-' in date:
        return f"{year:04}-{month:02}-{day:02}"
    elif '/' in date:
        return f"{day:02}/{month:02}/{year:04}"

def before(date: str) -> str:
    '''
    before() -> date for previous day in YYYY-MM-DD string format

    Return the date for the previous day of the given date in YYYY-MM-DD format.
    This function has been tested to work for year after 1582
    '''
    # Detect date format
    if '-' in date:
        year, month, day = (int(x) for x in date.split('-'))
    elif '/' in date:
        day, month, year = (int(x) for x in date.split('/'))
    else:
        raise ValueError("Invalid date format. Use YYYY-MM-DD or DD/MM/YYYY.")

    day -= 1  # previous day

    if day < 1:
        month -= 1
        if month < 1:
            year -= 1
            month = 12
        day = mon_max(month, year)

    # Return date in the same format as input
    if '-' in date:
        return f"{year:04}-{month:02}-{day:02}"
    elif '/' in date:
        return f"{day:02}/{month:02}/{year:04}"

def valid_date(date: str) -> bool:
    "Check validity of date"
    try:
        if '-' in date:
            year, month, day = (int(x) for x in date.split('-'))
        elif '/' in date:
            day, month, year = (int(x) for x in date.split('/'))
        else:
            raise ValueError("Invalid date format. Use YYYY-MM-DD or DD/MM/YYYY.")
        if not (1 <= month <= 12):
            return False
        if not (1 <= day <= mon_max(month, year)):
            return False
        return True
    except ValueError:
        return False

def usage():
    "Print a usage message to the user"
    print("Usage: " + str(sys.argv[0]) + " YYYY-MM-DD DIVISOR")
    sys.exit()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        usage()

    start_date = sys.argv[1]
    if not valid_date(start_date):
        print("Invalid date format. Please use YYYY-MM-DD.")
        usage()

    try:
        divisor = int(sys.argv[2])
        days_to_add_or_subtract = round(365 / divisor)

        # Calculate future date
        future_date = start_date
        for _ in range(days_to_add_or_subtract):
            future_date = after(future_date)

        # Calculate past date
        past_date = start_date
        for _ in range(days_to_add_or_subtract):
            past_date = before(past_date)

        print(f"A year divided by {divisor} is {days_to_add_or_subtract} days.")
        print(f"The date {days_to_add_or_subtract} days ago was {past_date}.")
        print(f"The date {days_to_add_or_subtract} days from now will be {future_date}.")

    except ValueError:
        print("Invalid divisor. Please provide a valid integer.")
        usage()

