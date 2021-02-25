#!/usr/bin/env python3
"""
Write a Python program to add two objects if both objects are an integer type.
"""

print("--- my solution ---")

def sum_obj(x, y):
    if isinstance(x, int) and isinstance(y, int):
        sum = x + y
        return sum
    else:
        return "The objects must be INT"

print(sum_obj(10, 20))

print("--- w3resource solution ---")

def add_numbers(a, b):
    if not (isinstance(a, int) and isinstance(b, int)):
         raise TypeError("Inputs must be integers")
    return a + b

print(add_numbers(10, 20))
