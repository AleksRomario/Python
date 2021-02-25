#!/usr/bin/env python3
"""
Write a Python program to test whether all numbers of a list is greater than a certain number. 
"""

print("--- my solution ---")



print("--- w3resource solution ---")

num = [2,3,4]
print()
print(all(x > 1 for x in num))
# Функция all возвращает True, если все элементы истинные (или объект пустой).
print(all(x > 4 for x in num))
print()
