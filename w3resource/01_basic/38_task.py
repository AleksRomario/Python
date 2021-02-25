#!/usr/bin/env python3
"""
Write a Python program to solve (x + y) * (x + y).
Test Data : x = 4, y = 3
Expected Output : (4 + 3) ^ 2) = 49
"""

print("--- my solution ---")

def plus(n1, n2):
    result = (n1 + n2 )* (n1 + n2)
    return result
print(plus(4, 3))

print("--- w3resource solution ---")
x, y = 4, 3
result = x * x + 2 * x * y + y * y
print("({} + {}) ^ 2) = {}".format(x, y, result))
