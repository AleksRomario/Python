#!/usr/bin/env python3
"""
Write a Python program to test whether a passed letter is a vowel or not. 
"""

print("--- my solution ---")
vowelList = ["a","e", "i", "o", "i"] 

def checkLetter(str):
    if str in vowelList:
        return "Vowel"
    return "Not a Vowel"

print(checkLetter("a"))
print(checkLetter("b"))

print("--- w3resource solution ---")

def is_vowel(char):
    all_vowels = 'aeiou'
    return char in all_vowels

print(is_vowel('c'))
print(is_vowel('e'))
