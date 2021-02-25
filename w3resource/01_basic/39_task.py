#!/usr/bin/env python3
"""
 Write a Python program to compute the future value of a specified principal amount, rate of interest, and a number of years.
Test Data : amt = 10000, int = 3.5, years = 7
Expected Output : 12722.79
"""

print("--- my solution ---")
# Do not know what formula to calculate was used 
amt = 10000
interest = 3.5
years = 7

total = ((10000 * 3.5 / 100) * 7 ) + 10000
print(total)

print("--- w3resource solution ---")

amt = 10000
interest = 3.5
years = 7

future_value  = amt*((1+(0.01*interest)) ** years)
print(round(future_value,2))
