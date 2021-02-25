#!/usr/bin/env python3
"""
Write a Python program to get the identity of an object.
"""

print("--- my solution ---")

x = "string"
print(id(x))


print("--- w3resource solution ---")

obj1 = object()
obj1_address = id(obj1)
print()
print(obj1_address)
print()


