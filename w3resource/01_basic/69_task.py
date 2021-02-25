#!/usr/bin/env python3
"""
Write a Python program to sort three integers without using conditional statements and loops.
"""

print("--- my solution ---")
print("Program will sort and output 3 integers given by user.")
x = int(input("Input your nuber: ")) 
y = int(input("Input your nuber: ")) 
z = int(input("Input your nuber: ")) 
n1 = min(x, y, z)
n3 = max(x, y, z)
n2 = x + y + z - n1 -n3
print("Sorted numbers {}, {}, {} = {}, {}, {}" .format(x, y, z, n1, n2, n3))



print("--- w3resource solution ---")
x = int(input("Input first number: "))
y = int(input("Input second number: "))
z = int(input("Input third number: "))

a1 = min(x, y, z)
a3 = max(x, y, z)
a2 = (x + y + z) - a1 - a3
print("Numbers in sorted order: ", a1, a2, a3)



