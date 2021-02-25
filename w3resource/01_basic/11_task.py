#!/usr/bin/env python3
"""
Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s). 
Sample function : abs()
Expected Result : 
abs(number) -> number
Return the absolute value of the argument.
"""
print("--- my solution ---")
# Do not finished by me. Directed wrong way
sample = input("Sample function : ")
sample = sample.split("()")
sample = str(sample[0])+".__doc__"
print(sample)


print("--- w3resource solution ---")
print(abs.__doc__)

"""
Python Docstring:

A docstring is a string literal that occurs as the first statement in a module, function, class, or method definition. Such a docstring becomes the __doc__ special attribute of that object.

All modules should normally have docstrings, and all functions and classes exported by a module should also have docstrings. Public methods (including the __init__ constructor) should also have docstrings.
"""
