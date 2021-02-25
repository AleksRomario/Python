#!/usr/bin/env python3
"""
Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference.
"""

print("--- my solution ---")
number = int(input("Type in the number to get difference between a given number and 17: "))

if number <= 17:
    print(17 - number)
else:
    print(abs(2*(number - 17)))
    

print("--- w3resource solution ---")

def difference(n):
    if n <= 17:
        return 17 - n
    else:
        return (n - 17) * 2

print(difference(22))
print(difference(14))


"""
Python if-else syntax:

if condition :
    indentedStatementBlockForTrueCondition
else:
    indentedStatementBlockForFalseCondition

"""

