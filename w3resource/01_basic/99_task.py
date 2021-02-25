#!/usr/bin/env python3
"""
Write a Python program to clear the screen or terminal.
"""

print("--- my solution ---")

import os, time 
print(os.name)
print( os.uname().sysname)
if os.uname().sysname == "Darwin":
    print("You are using macbook")
time.sleep(2)
os.system('clear')
time.sleep(2)

print("--- w3resource solution ---")

import os
import time
os.system("ls")
time.sleep(2)
os.system('clear')

