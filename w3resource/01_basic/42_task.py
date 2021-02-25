#!/usr/bin/env python3
"""
Write a Python program to determine if a Python shell is executing in 32bit or 64bit mode on OS.
"""

print("--- my solution ---")
# https://docs.python.org/3/library/struct.html

print("--- w3resource solution ---")

# For 32 bit it will return 32 and for 64 bit it will return 64
import struct
print(struct.calcsize("P") * 8)
