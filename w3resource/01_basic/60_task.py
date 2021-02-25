#!/usr/bin/env python3
"""
Write a Python program to calculate the hypotenuse of a right angled triangle.
c = √(a² + b²)
"""

print("--- my solution ---")
import math 

def hypotenuse(sideAB=4, sideBC=3 ):
    sideAC = math.sqrt((sideAB**2) + (sideBC**2))
    return sideAC

print(hypotenuse())


print("--- w3resource solution ---")


from math import sqrt
print("Input lengths of shorter triangle sides:")
a = float(input("a: "))
b = float(input("b: "))

c = sqrt(a**2 + b**2)
print("The length of the hypotenuse is", c )
