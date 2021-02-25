#!/usr/bin/env python3
"""
Write a Python program to get the n copies of the first 2 characters of a given string. Return the n copies of the whole string if the length is less than 2.
"""

print("--- my solution ---")

# did it my way, by returning whole string after coping first 2 characters
# recuired n times 

def stringEater(string, n):
    if len(string) <= 2:
        return string * n
    else:
        temp = string[:2]
        result = (temp * (n-1)) + string
        return result



string1 = "ab"
string2 = "abcdef"
string3 = "p"
stringEater(string1, 3)
print(stringEater(string1, 3))
print(stringEater(string2, 2))
print(stringEater(string3, 3))

print("--- w3resource solution ---")

def substring_copy(str, n):
  flen = 2
  if flen > len(str):
    flen = len(str)
  substr = str[:flen]

  result = ""
  for i in range(n):
    result = result + substr
  return result
print(substring_copy('abcdef', 2))
print(substring_copy('p', 3));
