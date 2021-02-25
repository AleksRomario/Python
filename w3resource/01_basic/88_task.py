#!/usr/bin/env python3
"""
Given variables x=30 and y=20, write a Python program to print "30+20=50"
"""

print("--- my solution ---")
x = 30 
y = 20
z = x + y 
print("old style")
print("%i + %i = %i" %(x, y, z))
print("new style:")
print("{0} + {1} = {2}" .format(x, y, z))
print("string interpolation:")
print(f"{x} + {y} = {(x+y)}")

print("--- w3resource solution ---")
x = 30
y = 20
print("\n%d+%d=%d" % (x, y, x+y))
print()


