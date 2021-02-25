#!/usr/bin/env python3
"""
Write a Python program to test whether the system is a big-endian platform or little-endian platform.
"""

print("--- my solution ---")

# https://pythonworld.ru/moduli/modul-sys.html
# sys.byteorder - порядок байтов. Будет иметь значение 'big' при порядке следования битов от старшего к младшему, и 'little', если наоборот (младший байт первый).

print("--- w3resource solution ---")

import sys
print()
if sys.byteorder == "little":
    #intel, alpha
    print("Little-endian platform.")
else:
    #motorola, sparc
    print("Big-endian platform.")
print()


