#!/usr/bin/env python3
"""
Write a Python program to print the current call stack
"""

print("--- my solution ---")



print("--- w3resource solution ---")

import traceback
print()
def f1():
    return abc()
def abc():
    traceback.print_stack()
f1()
print()


