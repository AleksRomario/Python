#!/usr/bin/env python3
"""
Write a Python program to get the name of the host on which the routine is running.
"""

print("--- my solution ---")
import socket
print(socket.gethostname())


print("--- w3resource solution ---")

import socket
host_name = socket.gethostname()
print()
print("Host name:", host_name)
print()
