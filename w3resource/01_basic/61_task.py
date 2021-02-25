#!/usr/bin/env python3
"""
Write a Python program to convert the distance (in feet) to inches, yards, and miles.
"""

print("--- my solution ---")

feet = int(input("Enter required feet distance: "))

def calculate(feet=0):
    inches = str(feet * 12)
    yards = str(feet / 3)
    miles = str(feet / 5280)
    print("The result of calculation of given feet is: \nInches = {}\nYards = {}\nMiles = {}".format(inches, yards, miles))


calculate(feet)


print("--- w3resource solution ---")

d_ft = int(input("Input distance in feet: "))
d_inches = d_ft * 12
d_yards = d_ft / 3.0
d_miles = d_ft / 5280.0

print("The distance in inches is %i inches." % d_inches)
print("The distance in yards is %.2f yards." % d_yards)
print("The distance in miles is %.2f miles." % d_miles)


