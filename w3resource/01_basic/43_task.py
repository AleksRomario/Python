#!/usr/bin/env python3
"""
Write a Python program to get OS name, platform and release information.

"""

print("--- my solution ---")
import os
import platform 
print(os.name)
print(platform.system())
print(platform.release())
#print(platform.mac_ver(release='', versioninfo=('', '', ''), machine=''))
print("--- w3resource solution ---")

import platform
import os
print(os.name)
print(platform.system())
print(platform.release())
