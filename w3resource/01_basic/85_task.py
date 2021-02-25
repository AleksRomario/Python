#!/usr/bin/env python3
"""
Write a Python program to check whether a file path is a file or a directory.
"""

print("--- my solution ---")
import os.path

is_directory = os.path.isdir('84_task') 
print("Is the path is directory: ", is_directory)
is_file = os.path.isfile('84_task.py')
print("Is the path is file: ", is_file)

print("--- w3resource solution ---")

import os
path="abc.txt"
if os.path.isdir(path):
    print("\nIt is a directory")
elif os.path.isfile(path):
    print("\nIt is a normal file")
else:
    print("It is a special file (socket, FIFO, device file)" )
print()

