#!/usr/bin/env python3
"""
Write a Python program to display your details like name, age, address in three different lines.
"""

print("--- my solution ---")

print("name \nage \nadress")


print("--- w3resource solution ---")

def personal_details():
    name, age = "Simon", 19
    address = "Bangalore, Karnataka, India"
    print("Name: {}\nAge: {}\nAddress: {}".format(name, age, address))

personal_details()
