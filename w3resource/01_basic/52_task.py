#!/usr/bin/env python3
from __future__ import print_function
"""
Write a Python program to print to stderr.
"""

print("--- my solution ---")

print("--- w3resource solution ---")

# from __future__ import print_function
import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

eprint("abc", "efg", "xyz", sep="--")
