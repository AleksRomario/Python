#!/usr/bin/env python3
"""
Write a Python program to concatenate all elements in a list into a string and return it.
"""

print("--- my solution ---")

def makeString(data):
    string = ""
    for i in data:
        string += str(i)
    return string

myList = [5, 1, 6, 5, 3, 4]
print(makeString(myList))
print(makeString([1, 5, 12, 2]))

print("--- w3resource solution ---")

def concatenate_list_data(list):
    result= ''
    for element in list:
        result += str(element)
    return result

print(concatenate_list_data([1, 5, 12, 2]))
