#!/usr/bin/env python3
"""
Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.
"""

print("--- my solution ---")

def sum_of_three(x, y, z):
    sum = 0
    if x == y or x == z or y == z:
        return sum
    else:
        sum = x + y + z 
        return sum 

print(sum_of_three(2, 1, 2))
print(sum_of_three(3, 2, 2))
print(sum_of_three(2, 2, 2))
print(sum_of_three(1, 2, 3))

print("--- w3resource solution ---")

def sum(x, y, z):
    if x == y or y == z or x==z:
        sum = 0
    else:
        sum = x + y + z
    return sum

print(sum(2, 1, 2))
print(sum(3, 2, 2))
print(sum(2, 2, 2))
print(sum(1, 2, 3))
