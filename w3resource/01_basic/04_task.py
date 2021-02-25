#!/usr/bin/env python3
"""
Write a Python program which accepts the radius of a circle from the user 
and compute the area. 

Sample Output :
r = 1.1
Area = 3.8013271108436504
"""
import math

radius = float(input("Type in radius: "))
print("r =", radius)
result = math.pi * radius**2
print("Area =", result)
