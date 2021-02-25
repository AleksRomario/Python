#!/usr/bin/env python3
"""
Write a Python program to count the number occurrence of a specific character in a string.
"""

print("--- my solution ---")

teststring = "abracadabra"
s = "The quick brown fox jumps over the lazy dog."

def counting(s):
    result = 0
    for l in s:
        if l == "o":
            result += 1
    return result

print(counting(teststring))
print(counting(s))
print("--- w3resource solution ---")


s = "The quick brown fox jumps over the lazy dog."
print()
print(s.count("o"))
print()

