#!/usr/bin/env python3
"""
Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5.
"""

print("--- my solution ---")

def sum_dif(n1, n2):
    if n1 == n2:
        return True 
    elif n1 + n2 == 5:
        return True
    elif n1 - n2 == 5 or n2 - n1 == 5:
        return True
    else:
        return False 

print(sum_dif(7, 2))
print(sum_dif(3, 2))
print(sum_dif(2, 2))
print("--- w3resource solution ---")

def test_number5(x, y):
    if x == y or abs(x-y) == 5 or (x+y) == 5:
        return True
    else:
        return False

print(test_number5(7, 2))
print(test_number5(3, 2))
print(test_number5(2, 2))
