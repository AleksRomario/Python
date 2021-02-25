#!/usr/bin/env python3
"""
Write a python program to call an external command in Python.
https://docs.python.org/3/library/subprocess.html#module-subprocess
https://pythonworld.ru/moduli/modul-subprocess.html
"""

print("--- my solution ---")
import subprocess 
subprocess.run(["ls", "-l"])
subprocess.call(["ls", "-l"])


print("--- w3resource solution ---")

from subprocess import call
call(["ls", "-l"])
