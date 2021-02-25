#!/usr/bin/env python3
"""
Write a Python program to determine profiling of Python programs. 
Note: A profile is a set of statistics that describes how often and for how long various parts of the program executed. These statistics can be formatted into reports via the pstats module.
https://docs.python.org/3/library/profile.html
"""


print("--- my solution ---")

print("--- w3resource solution ---")

import cProfile
def sum():
    print(1+2)
cProfile.run('sum()')
