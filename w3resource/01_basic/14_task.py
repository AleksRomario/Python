#!/usr/bin/env python3
"""
Write a Python program to calculate number of days between two dates.
Sample dates : (2014, 7, 2), (2014, 7, 11)
Expected output : 9 days 
"""

print("--- my solution ---")
import datetime 
from_date = datetime.date(2014, 7, 2)
to_date = datetime.date(2014, 7, 11)
difference = to_date - from_date
print(" Expected output :", difference.days, "days")

print("--- w3resource solution ---")

from datetime import date
f_date = date(2014, 7, 2)
l_date = date(2014, 7, 11)
delta = l_date - f_date
print(delta.days)

"""
Python datetime.date(year, month, day) :

The function returns date object with same year, month and day. All arguments are required. Arguments may be integers, in the following ranges:

MINYEAR <= year <= MAXYEAR
1 <= month <= 12
1 <= day <= number of days in the given month and year
If an argument outside those ranges is given, ValueError is raised.

Note: The smallest year number allowed in a date or datetime object. MINYEAR is 1.
The largest year number allowed in a date or datetime object. MAXYEAR is 9999.
"""
