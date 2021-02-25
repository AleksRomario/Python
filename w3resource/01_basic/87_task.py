#!/usr/bin/env python3
"""
Write a Python program to get the size of a file.
"""

print("--- my solution ---")
import os 
print(os.stat('85_task.py'))
size = os.stat('85_task.py').st_size
print(size)

print("--- w3resource solution ---")

import os
file_size = os.path.getsize("85_task.py")
print("\nThe size of abc.txt is :",file_size,"Bytes")
print()

