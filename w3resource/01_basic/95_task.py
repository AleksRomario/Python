#!/usr/bin/env python3
"""
Write a Python program to check whether a string is numeric
"""

print("--- my solution ---")

num_str = "123"
non_num_str = "abc"
num_char_str = "abc123"

def check(str):
    if str.isalpha():
        print("string with characters only")
    elif str.isdecimal():
        print("string with digits only")
    elif str.isalnum:
        print("string with characters and numbers")
    else:
        print("String with unknown symbols")

check(num_str)
check(non_num_str)
check(num_char_str)

print("--- w3resource solution ---")

str = 'a123'
#str = '123'
try:
    i = float(str)
except (ValueError, TypeError):
    print('\nNot numeric')
print()
