#!/usr/bin/env python3
"""
Write a Python program to test whether a number is within 100 of 1000 or 2000.
https://www.w3resource.com/python-exercises/python-basic-exercise-17.php
"""

print("--- my solution ---")

# misinterpreted the task and because of that it is done wrong

n = int(input("input your number: "))

def checkNumber(n):
    if n >= 100 and n < 1000:
        print("the number is between 100 and 1000")
    elif n >= 1000 and n < 2000:
        print("the number is between 1000 and 2000")
    else:
        print("number is out of boundaries")

checkNumber(n)

print("--- w3resource solution ---")

def near_thousand(n):
      return ((abs(1000 - n) <= 100) or (abs(2000 - n) <= 100))
print(near_thousand(1000))
print(near_thousand(900))
print(near_thousand(800))   
print(near_thousand(2200))

"""
Python abs(x) function:

The function returns the absolute value of a number. The argument may be an integer or a floating point number. If the argument is a complex number, its magnitude is returned.

"""
