#!/usr/bin/env python3
"""
Write a Python program to perform an action if a condition is true.
Given a variable name, if the value is 1, display the string "First day of a Month!" and do nothing if the value is not equal.
"""

print("--- my solution ---")

def to_tell(n):
    if n == 1:
        print("First day of the month")

to_tell(1)
to_tell(2)

print("--- w3resource solution ---")

n=1
if n == 1:
    print("\nFirst day of a month")
print()


