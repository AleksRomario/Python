#!/usr/bin/env python3
"""
Write a Python program to list all files in a directory in Python.
"""

print("--- my solution ---")
import subprocess 
result = subprocess.run(["ls", "-l"])
print(result)
print("--- w3resource solution ---")

from os import listdir
from os.path import isfile, join
files_list = [f for f in listdir('../01_basic') if isfile(join('../01_basic', f))]
print(type(files_list))
files_list = sorted(files_list)
print(files_list);

