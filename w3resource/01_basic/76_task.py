#!/usr/bin/env python3
"""
Write a Python program to get the command-line arguments (name of the script, the number of arguments, arguments) passed to a script.
"""

print("--- my solution ---")



print("--- w3resource solution ---")

import sys
print("This is the name/path of the script:"),sys.argv[0]
print("Number of arguments:",len(sys.argv))
print("Argument List:",str(sys.argv))
# command executed in command prompt:
# python 76_task.py arg1 arg2 arg3

