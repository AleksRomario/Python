#!/usr/bin/env python3
"""
Write a Python program to get a string which is n (non-negative integer) copies of a given string.
"""

print("--- my solution ---")

string = input("how many copies of the string do you need? : ")
print(string * int(string))

print("--- w3resource solution ---")


def larger_string(str, n):
   result = ""
   for i in range(n):
      result = result + str
   return result

print(larger_string('abc', 2))
print(larger_string('.py', 3))
