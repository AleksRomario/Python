#!/usr/bin/env python3
"""
Write a Python program to get an absolute file path.

"""

print("--- my solution ---")
import os 
path = os.path.abspath("63_task.py")
print("absolute path is ", path)
print("--- w3resource solution ---")

def absolute_file_path(path_fname):
        import os
        return os.path.abspath(path_fname)        
print("Absolute file path: ",absolute_file_path("63_task.py"))
