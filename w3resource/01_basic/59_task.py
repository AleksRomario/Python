#!/usr/bin/env python3
"""
Write a Python program to convert height (in feet and inches) to centimeters
"""

print("--- my solution ---")
 
def inches_feets_to_cm(inche=0, feet=0):
    cm1 = inche * 2.54
    cm2 = feet * 30.48 
    return cm1 + cm2
print(inches_feets_to_cm(3, 5))

print("--- w3resource solution ---")

print("Input your height: ")
h_ft = int(input("Feet: "))
h_inch = int(input("Inches: "))

h_inch += h_ft * 12
h_cm = round(h_inch * 2.54, 1)

print("Your height is : %d cm." % h_cm)


