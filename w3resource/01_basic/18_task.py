#!/usr/bin/env python3
"""
Write a Python program to calculate the sum of three given numbers, if the values are equal then return three times of their sum.
"""

print("--- my solution ---")
n1 = int(input("First number: "))
n2 = int(input("Second number: "))
n3 = int(input("Third number: "))

def sumOfThree(x, y, z):
    if x == y and x == z:
        return (x + y + z) * 3
    else:
        return x + y + z 

print(sumOfThree(n1, n2, n3))

print("--- w3resource solution ---")

def sum_thrice(x, y, z):

     sum = x + y + z

     if x == y == z:
      sum = sum * 3
     return sum

print(sum_thrice(1, 2, 3))
print(sum_thrice(3, 3, 3))
