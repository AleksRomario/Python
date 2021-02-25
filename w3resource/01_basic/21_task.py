#!/usr/bin/env python3
"""
Write a Python program to find whether a given number (accept from the user) is even or odd, print out an appropriate message to the user.
"""

print("--- my solution ---")

number = int(input("Give me the number: "))

def checkNumber(number):
    
    if number % 2 == 0 or number == 0:
        print("Your number is even")
    else:
        print("Your number is odd")
        
checkNumber(number)

print("--- w3resource solution ---")
num = int(input("Enter a number: "))
mod = num % 2
if mod > 0:
    print("This is an odd number.")
else:
    print("This is an even number.")
