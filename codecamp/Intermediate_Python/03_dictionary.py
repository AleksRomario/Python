#!/usr/bin/env python3
# Based on freeCodeCamp.org video tutorial - Intermediate Python Programming Course


# Dictionary: Key-Value pairs, Unordered, mutable


# 1.1 Creation 
print("1.1", "Dictionary creation")
myDict = {"name" : "Alex", "age" : 39 , "city": "Riga"}
print("1.1", type(myDict), myDict)


# 1.2 Creating Dictionary using function 
print("Creating Dictionary with function")
d = dict(name="Alex", age=39, city="Rige")
print("1.2", type(d), d)


# 1.3 Acessing value by key
print("Acess value by key")
res1 = d["name"]
res2 = d["age"]
res3 = d["city"]
print("1.3", "Access name =",  res1)
print("1.3", "Access age =",  res2)
print("1.3", "Access city =",  res3)
# Accessing by non existing key will give an error (KeyError)


# 1.4 Adding key-value 
print("Adding key and value")
print("1.4", "Original Dictionary", d)
d["mail"] = "romario@mail.com"
print("1.4", "Dictionary after adding", d)


# 1.5 Changing value 
print("Changing value")
print("1.5", "Original Dictionary", d)
d["mail"] = "romario@gmal.com"
print("1.5", "Changed Dictionary", d)


# 1.6 Deleting value using del 
print("Deleting values using del")
print("1.6", "Original", d)
del d["mail"]
print("1.6", "After deletion", d)
d["mail"] = "romario@gmal.com"


# 1.7 Deleting value using pop method 
print("Deleting values using pop")
print("1.7", "Original", d)
r = d.pop("mail")
print("1.7", "After deletion", d)
# if assigned , will return value
print("1.7", "Returned value", r)
d["mail"] = "romario@gmal.com"


# 1.8 Deleting value using popitem method 
print("Deleting values using popitem")
print("1.8", "Original", d)
r = d.popitem()
print("1.8", "After deletion", d)
# if assigned , will return value
print("1.8", "Returned value pair",type(r), r)


# 1.9 Checking if a key in dictionary 
print("Check if key in Dictionary")
if "name" in d:
    print("1.9", d["name"])
else:
    print("1.9","No")
# Can be used try statement
try:
    print("1.9", d["name"])
except:
    print("Error")


# 1.10 Loop Dictionary 
print("Loop Dictionary")
print("print key")
for key in d:
    print("1.10", key)

print("print key")
for key in d.keys():
    print("1.10", key)

print("print value")
for value in d.values():
    print("1.10", value)

print("print key and value")
for key in d:
    print("1.10", "key =", key, "Value =", d[key])

print("print key and value")
for key, value in d.items():
    print("1.10", "key =", key, "Value =", value)


# 1.11 Copy Dictionaty 
print("Copy dictionary usinf copy()")
print("1.11", "Original dictionary", d)
d2 = d.copy()
print("1.11", "Copied dictionary", d2)
d2["sex"] = "male"
print("1.11", "Original dictionary", d)
print("1.11", "Copied dictionary + modified", d2)
# If you try to assign as variable , both dictionaries will point to one memery allocation


# 1.12 Copy by using dict() method
print("Copy dictionary usinf copy()")
print("1.11", "Original dictionary", d)
d2 = dict(d)
print("1.11", "Copied dictionary", d2)
d2["sex"] = "Male"
print("1.11", "Copied dictionary + modified", d2)


# 1.13 Merge 2 dictionaries
print("Merging two dictionaries")
dOne = dict(first="One", second="two")
dTwo = dict(third="Three")
print("1.13", "First dictionary", dOne)
print("1.13", "Second dictionary", dTwo)
dOne.update(dTwo)
print("1.13", "After merging", dOne)


# 1.14 key can be tuple 
print("Example of that key can be tuple (immutable value)")
t = (1, 2)
td = {t : "valueName"}
print("1.14", "Dictionary: ", td)

"""
class dict(object)
 |  dict() -> new empty dictionary
 |  dict(mapping) -> new dictionary initialized from a mapping object's
 |      (key, value) pairs
 |  dict(iterable) -> new dictionary initialized as if via:
 |      d = {}
 |      for k, v in iterable:
 |          d[k] = v
 |  dict(**kwargs) -> new dictionary initialized with the name=value pairs
 |      in the keyword argument list.  For example:  dict(one=1, two=2)


 |  clear(...)
 |      D.clear() -> None.  Remove all items from D.
 |
 |  copy(...)
 |      D.copy() -> a shallow copy of D
 |
 |  get(self, key, default=None, /)
 |      Return the value for key if key is in the dictionary, else default.
 |
 |  items(...)
 |      D.items() -> a set-like object providing a view on D's items
 |
 |  keys(...)
 |      D.keys() -> a set-like object providing a view on D's keys
 |
 |  pop(...)
 |      D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
 |      If key is not found, d is returned if given, otherwise KeyError is raised
 |
 |  popitem(self, /)
 |      Remove and return a (key, value) pair as a 2-tuple.
 |
 |      Pairs are returned in LIFO (last-in, first-out) order.
 |      Raises KeyError if the dict is empty.
 |
 |  setdefault(self, key, default=None, /)
 |      Insert key with a value of default if key is not in the dictionary.
 |
 |      Return the value for key if key is in the dictionary, else default.
 |
 |  update(...)
 |      D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.
 |      If E is present and has a .keys() method, then does:  for k in E: D[k] = E[k]
 |      If E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v
 |      In either case, this is followed by: for k in F:  D[k] = F[k]
 |  
 |  values(...)
 |      D.values() -> an object providing a view on D's values
 |
***********
 |
 |  Class methods defined here:
 |  
 |  fromkeys(iterable, value=None, /) from builtins.type
 |      Create a new dictionary with keys from iterable and values set to value.

"""

