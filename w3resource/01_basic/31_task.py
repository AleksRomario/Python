#!/usr/bin/env python3
"""
Write a Python program to compute the greatest common divisor (GCD) of two positive integers.
"""

print("--- my solution ---")

def mygcd(n1, n2):
    pass
    if n1 > n2:
        while n1 > 0:
            n1 = n1 - n2

mygcd(12, 17)
mygcd(4, 6)


print("--- w3resource solution ---")

def gcd(x, y):
    gcd = 1

    if x % y == 0:
        return y

    for k in range(int(y / 2), 0, -1):
        if x % k == 0 and y % k == 0:
            gcd = k
            break
    return gcd

print(gcd(12, 17))
print(gcd(4, 6))
