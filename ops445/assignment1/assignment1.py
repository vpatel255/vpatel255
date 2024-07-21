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
    day, month, year = (int(x) for x in date.split('/'))
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
    after() -> date for next day in DD/MM/YYYY string format

    Return the date for the next day of the given date in DD/MM/YYYY format.
    This function has been tested to work for year after 1582
    '''
    day, month, year = (int(x) for x in date.split('/'))
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
    return f"{day:02}/{month:02}/{year:04}"

def before(date: str) -> str:
    "Returns previous day's date as DD/MM/YYYY"
    day, month, year = (int(x) for x in date.split('/'))
    day -= 1

    if day < 1:
        month -= 1
        if month < 1:
            year -= 1
            month = 12
        day = mon_max(month, year)

    return f"{day:02}/{month:02}/{year:04}"

def valid_date(date: str) -> bool:
    "Check validity of date"
    try:
        day, month, year = (int(x) for x in date.split('/'))
        if not (1 <= month <= 12):
            return False
        if not (1 <= day <= mon_max(month, year)):
            return False
        return True
    except ValueError:
        return False

def day_count(start_date: str, end_date: str) -> int:
    "Counts the number of weekend days between start_date and end_date (inclusive)"
    if not valid_date(start_date) or not valid_date(end_date):
        raise ValueError("Invalid date format. Please use DD/MM/YYYY.")

    count = 0
    current_date = start_date
    while True:
        if day_of_week(current_date) in ['Sat', 'Sun']:
            count += 1
        if current_date == end_date:
            break
        current_date = after(current_date)

    return count

def usage():
    "Print a usage message to the user"
    print("Usage: " + str(sys.argv[0]) + " DD/MM/YYYY DD/MM/YYYY")
    sys.exit()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        usage()

    start_date = sys.argv[1]
    end_date = sys.argv[2]

    if not valid_date(start_date) or not valid_date(end_date):
        print("Invalid date format. Please use DD/MM/YYYY.")
        usage()

    try:
        count = day_count(start_date, end_date)
        print(f"The period between {start_date} and {end_date} includes {count} weekend days.")
    except ValueError as e:
        print(e)
        usage()

