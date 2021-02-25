#!/usr/bin/env python3
"""
Write a python program to access environment variables.
"""

print("--- my solution ---")

print("--- w3resource solution ---")

import os
# Access all environment variables
print('*----------------------------------*')
print(os.environ)
print('*----------------------------------*')
# Access a particular environment variable
print(os.environ['HOME'])
print('*----------------------------------*')
print(os.environ['PATH'])
print('*----------------------------------*')
