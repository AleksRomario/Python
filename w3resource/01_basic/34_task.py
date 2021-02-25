#!/usr/bin/env python3
"""
Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20.
"""

print("--- my solution ---")

def sum_of_two(n1, n2):
    sum = n1 + n2
    if sum < 20 and sum > 15:
        sum = 20
    return  sum 

print(sum_of_two(10, 6))
print(sum_of_two(10, 2))
print(sum_of_two(10, 12))

print("--- w3resource solution ---")

def sum(x, y):
    sum = x + y
    if sum in range(15, 20):
        return 20
    else:
        return sum

print(sum(10, 6))
print(sum(10, 2))
print(sum(10, 12))
