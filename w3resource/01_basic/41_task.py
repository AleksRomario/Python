#!/usr/bin/env python3
"""
Write a Python program to check whether a file exists.
"""

print("--- my solution ---")

import os.path
if os.path.isfile("41_task.py"):
    print("File exists")
else:
    print("File do not exist")

print("--- w3resource solution ---")

import os.path
open('abc.txt', 'w')
print(os.path.isfile('abc.txt'))
