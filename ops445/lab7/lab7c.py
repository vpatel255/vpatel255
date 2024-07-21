#!/usr/bin/env python3

class Time:
   """Simple object type for time of the day.
      data attributes: hour, minute, second
   """
   def __init__(self, hour=12, minute=0, second=0):
       """Constructor for time object"""
       self.hour = hour
       self.minute = minute
       self.second = second

def format_time(t):
    """Return time object (t) as a formatted string"""
    return f'{t.hour:02d}:{t.minute:02d}:{t.second:02d}'

def sum_times(t1, t2):
    """Add two time objects and return the sum."""
    total_seconds = time_to_sec(t1) + time_to_sec(t2)
    return sec_to_time(total_seconds)

def valid_time(t):
    """Check for the validity of the time object attributes:
       0 <= hour < 24, 0 <= minute < 60, 0 <= second < 60
    """
    if not (0 <= t.hour < 24 and 0 <= t.minute < 60 and 0 <= t.second < 60):
        return False
    return True

def change_time(time, seconds):
    """Change the time object by a number of seconds."""
    total_seconds = time_to_sec(time) + seconds
    if total_seconds < 0:
        total_seconds = 0
    elif total_seconds >= 86400:
        total_seconds = 86399
    new_time = sec_to_time(total_seconds)
    time.hour = new_time.hour
    time.minute = new_time.minute
    time.second = new_time.second
    return None

def time_to_sec(time):
    """Convert a time object to a single integer representing the number of seconds from mid-night."""
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds

def sec_to_time(seconds):   
    """Convert a given number of seconds to a time object in hour, minute, second format."""
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time

