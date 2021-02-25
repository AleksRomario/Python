#!/usr/bin/env python3
"""
Write a Python program to check whether a specified value is contained in a group of values.
3 -> [1, 5, 8, 3] : True
-1 -> [1, 5, 8, 3] : False
"""

print("--- my solution ---")
def inList(n, list):
    return n in list

print(inList(3, [1, 5, 8, 3]))
print(inList(-1, [1, 5, 8, 3]))

print("--- w3resource solution ---")

def is_group_member(group_data, n):
    for value in group_data:
        if n == value:
            return True
    return False
print(is_group_member([1, 5, 8, 3], 3))
print(is_group_member([5, 8, 3], -1))
