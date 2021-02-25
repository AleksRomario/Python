#!/usr/bin/env python3
"""
Write a Python program to get system command output.
"""

print("--- my solution ---")



print("--- w3resource solution ---")
import subprocess
# file and directory listing
returned_text = subprocess.check_output("ls ..", shell=True, universal_newlines=True)
print("dir command to list file and directory")
print(returned_text)

