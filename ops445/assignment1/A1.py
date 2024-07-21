#!/usr/bin/env python3
import sys

def leap_year(year):
    """Return True if year is a leap year, False otherwise."""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def mon_max(month, year):
    """Return the maximum number of days in a given month and year."""
    days_in_month = [31, 28 + leap_year(year), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return days_in_month[month - 1]

def after(date):
    """Return the next date after the given date."""
    year, month, day = map(int, date.split('-'))
    
    # Increment day
    day += 1
    
    # Check if day exceeds the maximum days in the month
    if day > mon_max(month, year):
        day = 1
        month += 1
        if month > 12:
            month = 1
            year += 1
    
    return f"{year:04d}-{month:02d}-{day:02d}"

# Test code
if __name__ == "__main__":
    # Replace with actual test cases or integrate with your test framework
    print(after('2023-01-31'))  # Should print 2023-02-01
    print(after('2023-02-28'))  # Should print 2023-03-01
    print(after('2023-12-31'))  # Should print 2024-01-01

    # Test leap_year() and mon_max()
    print(leap_year(2020))  # Should print True
    print(leap_year(2021))  # Should print False
    print(mon_max(2, 2020))  # Should print 29 (February in a leap year)
    print(mon_max(2, 2021))  # Should print 28 (February in a non-leap year)

