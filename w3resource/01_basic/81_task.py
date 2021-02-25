#!/usr/bin/env python3
"""
Write a Python program to concatenate N strings.
"""

print("--- my solution ---")


def concatenate(n):
    string = ""
    for i in range(n):
        string += "a"
    return string 
print(concatenate(6))

print("--- w3resource solution ---")

list_of_colors = ['Red', 'White', 'Black']
colors = '-'.join(list_of_colors)
print()
print("All Colors: "+colors)
print()

