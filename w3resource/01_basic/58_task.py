#!/usr/bin/env python3
"""
Write a python program to find the sum of the first n positive integers.
"""

print("--- my solution ---")

def sum_of_numbers(n):
    sum = 0
    for i in range(1, n+1):
        sum = sum + i
    return sum
print(sum_of_numbers(25))
# print(sum_of_numbers(2))



print("--- w3resource solution ---")
n = int(input("Input a number: "))
sum_num = (n * (n + 1)) / 2
print(sum_num)
