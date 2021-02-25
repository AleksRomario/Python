#!/usr/bin/env python3
"""
Write a Python program to create a histogram from a given list of integers.
"""

print("--- my solution ---")

def makeHistogram(list):
    for n in range(len(list)):
        times = list[n]
        print("@" * times)

makeHistogram([2, 3, 6, 5])

print("--- w3resource solution ---")

def histogram( items ):
    for n in items:
        output = ''
        times = n
        while( times > 0 ):
          output += '*'
          times = times - 1
        print(output)

histogram([2, 3, 6, 5])
