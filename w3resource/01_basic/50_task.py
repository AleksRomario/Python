#!/usr/bin/env python3
"""
Write a Python program to print without newline or space.
"""

print("--- my solution ---")
mystring = "hello my name is."
# mylist = list(mystring)
mystring = mystring.split(" ")
print(type(mystring))
print(mystring)
for i in range(len(mystring)):
        print(mystring[i], end="")
print("\n")

print("--- w3resource solution ---")

for i in range(0, 10):
    print('*', end="")
print("\n")
