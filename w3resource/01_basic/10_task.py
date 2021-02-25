#!/usr/bin/env python3
"""
Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
Sample value of n is 5 
Expected Result : 615
"""
print("--- my solution ---")
number = input("Enter number: ")
print("Sample value of n is %s" %number)
n  = number
nn = number + number
nnn = number * 3
result = int(n) + int(nn) + int(nnn)
print("Expected Result : %i"%result)

print("--- w3resource solution ---")
a = int(input("Input an integer : "))
n1 = int( "%s" % a )
n2 = int( "%s%s" % (a,a) )
n3 = int( "%s%s%s" % (a,a,a) )
print (n1+n2+n3)

"""
Python int(x, base=10):

The function returns an integer object constructed from a number or string x, or return 0 if no arguments are given. If x is a number, return x.__int__(). For floating point numbers, this truncates towards zero.

If x is not a number or if base is given, then x must be a string, bytes, or bytearray instance representing an integer literal in radix base
The literal can be preceded by + or - (with no space in between) and surrounded by whitespace
A base-n literal consists of the digits 0 to n-1, with a to z (or A to Z) having values 10 to 35. The default base is 10.
The allowed values are 0 and 2-36. Base-2, -8, and -16 literals can be optionally prefixed with 0b/0B, 0o/0O, or 0x/0X, as with integer literals in code.

"""
