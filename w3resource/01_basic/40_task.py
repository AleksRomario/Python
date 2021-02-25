#!/usr/bin/env python3
"""
Write a Python program to compute the distance between the points (x1, y1) and (x2, y2).
"""

print("--- my solution ---")
import math 

point1 = [2, 3]
point2 = [3, 2]

distance = math.sqrt(((point1[0]- point2[0])**2)+ ((point1[1] - point2[1])**2))
print(distance)


print("--- w3resource solution ---")

import math
p1 = [4, 0]
p2 = [6, 6]
distance = math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) )

print(distance)
