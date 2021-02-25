#!/usr/bin/env python3
"""
Write a Python program to print the calendar of a given month and year.
Note : Use 'calendar' module. 
"""
print("--- my solution ---")
import calendar 
year = int(input("Type in required year: "))
month = int(input("Type in required month: "))
show = calendar.TextCalendar().formatmonth(year, month)
print(show)

print("--- w3resource solution ---")
import calendar
y = int(input("Input the year : "))
m = int(input("Input the month : "))
print(calendar.month(y, m))

"""
Python calendar.month(theyear, themonth, w=0, l=0):

The function returns a month’s calendar in a multi-line string using the formatmonth() of the TextCalendar class.

'l' specifies the number of lines that each week will use.
"""
