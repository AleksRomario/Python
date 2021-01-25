#!/usr/bin/env python3

PI = 3.1415

def max2(a, b):
         return a if(a > b) else b

def max3(a, b, c):
         return max2(a, max2(b, c))

def sum(*vals):
         S = 0
         for x in vals:
                   S += x
         return S

def sayHello():
    msg = "Hello, this is mymath module: "
    print(msg)


if __name__ == "__main__":
    sayHello()
