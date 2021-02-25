#!/usr/bin/env python3
"""
Write a Python program to calculate the sum over a container.
"""

print("--- my solution ---")

container = [10, 20, 30]

def sum_list(l):
    result = 0
    for i in range(len(l)):
        result += l[i]    
    return result

print(sum_list(container))

print("--- w3resource solution ---")

s = sum([10,20,30])
print("\nSum of the container: ", s)
print()

