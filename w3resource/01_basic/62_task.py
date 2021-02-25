#!/usr/bin/env python3
"""
Write a Python program to convert all units of time into seconds.
"""

print("--- my solution ---")

days = int(input("Input required days: "))
hours = int(input("Input required hours: "))
minutes = int(input("Input required minutes: "))
seconds = int(input("Input required seconds: "))
def timeConvertion(days = 0, hours = 0, minutes = 0, seconds = 0):
    r_days = days * 3600 * 24 
    r_hours = hours * 3600 
    r_minutes = minutes * 60
    r_seconds = seconds
    result = r_days + r_hours + r_minutes + r_seconds
    return result

result = timeConvertion(days, hours, minutes, seconds)
print("Result in seconds: ", result)


print("--- w3resource solution ---")

days = int(input("Input days: ")) * 3600 * 24
hours = int(input("Input hours: ")) * 3600
minutes = int(input("Input minutes: ")) * 60
seconds = int(input("Input seconds: "))

time = days + hours + minutes + seconds

print("The  amounts of seconds", time)

