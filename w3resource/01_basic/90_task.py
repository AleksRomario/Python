#!/usr/bin/env python3
"""
Write a Python program to swap two variables.
"""

print("--- my solution ---")
x = 10 
y = 20
print("x before =", x)
print("y before =", y)
x, y = y, x  
print("x after =", x)
print("y after =", y)

print("--- w3resource solution ---")

a = 30
b = 20
print("\nBefore swap a = %d and b = %d" %(a, b))
a, b = b, a
print("\nAfter swaping a = %d and b = %d" %(a, b))
print()


"""
Python: swapping two variables

Swapping two variables refers to mutually exchanging the values of the variables. Generally, this is done with the data in memory.

The simplest method to swap two variables is to use a third temporary variable :

define swap(a, b)
    temp := a
    a := b
    b := temp
"""
