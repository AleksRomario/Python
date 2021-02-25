#!/usr/bin/env python3
"""
Write a Python program to get a new string from a given string where "Is" has been added to the front. If the given string already begins with "Is" then return the string unchanged.
"""

print("--- my solution ---")
string = input("type in the string: ")
check = "Is"
def checkString(x):

    if check == x[:2]:
        return x
    else:
        return check + x

print(checkString(string))

print("--- w3resource solution ---")

def new_string(str):
  if len(str) >= 2 and str[:2] == "Is":
    return str
  return "Is" + str

print(new_string("Array"))
print(new_string("IsEmpty"))
