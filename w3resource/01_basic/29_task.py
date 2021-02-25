#!/usr/bin/env python3
"""
Write a Python program to print out a set containing all the colors from color_list_1 which are not present in color_list_2.

Test Data :
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
Expected Output :
{'Black', 'White'}


"""

print("--- my solution ---")

A = set(["White", "Black", "Red"])
B = set(["Red", "Green"])
C = A - B
print(C)

print("--- w3resource solution ---")

color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])

print(color_list_1.difference(color_list_2))
