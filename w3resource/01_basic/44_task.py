#!/usr/bin/env python3
"""
Write a Python program to locate Python site-packages
"""

print("--- my solution ---")
import sys
site_packages = next(p for p in sys.path if 'site-packages' in p)
print (site_packages)

print("--- w3resource solution ---")

import site;
print(site.getsitepackages())
