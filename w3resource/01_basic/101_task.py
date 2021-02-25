#!/usr/bin/env python3
"""
Write a Python program to access and print a URL's content to the console.
"""

print("--- my solution ---")



print("--- w3resource solution ---")

from http.client import HTTPConnection
conn = HTTPConnection("example.com")
conn.request("GET", "/")  
result = conn.getresponse()
# retrieves the entire contents.  
contents = result.read() 
print(contents)
