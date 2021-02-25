#!/usr/bin/env python3
"""
Write a Python program to calculate the sum of the digits in an integer.
"""

print("--- my solution ---")

number = input("Input required numer: ")
result = 0
for i in number:
    result += int(i)
    print(i, result)
print("result is : ", result)


print("--- w3resource solution ---")
num = int(input("Input a four digit numbers: "))
x  = num //1000
x1 = (num - x*1000)//100
x2 = (num - x*1000 - x1*100)//10
x3 = num - x*1000 - x1*100 - x2*10
print("The sum of digits in the number is", x+x1+x2+x3)

