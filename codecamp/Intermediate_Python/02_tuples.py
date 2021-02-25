#!/usr/bin/env python3
# Based on freeCodeCamp.org video tutorial - Intermediate Python Programming Course


# Tuples: ordered, immutable, allows duplicate elements
# Difference between Lists, Tuples can't be change after creation 

# 1.1 Tuples creation. (coma separated data)

myTuple1 = ("Alex", 39, "Riga")
# parenthesis are optional
myTuple2 = ("Alex", 39, "Riga")
print("Creation of the tuple")
print("1.1", type(myTuple1), myTuple1)
print("1.1", type(myTuple2), myTuple2)
# to create 1 element in a tuple , you need to create it with comma seperator otherwise it will be a str 
myTuple1 = ("Alex",)
myTuple2 = ("Alex")


# 1.2 Create with one element
print("Creation of the tuple with one element in it")
print("1.2", type(myTuple1), myTuple1)
print("1.2", type(myTuple2), myTuple2)


# 1.3 Creating with built-in function from iterable (like list)
print("Creating by function")
myTuple = tuple([1, 2, 3, 4])
print("1.3", type(myTuple1), myTuple)


# 1.4 Accessing element by refering to element by index
myTuple = ("Alex", 39, "Riga")
res = myTuple[1]
print("Accessing by index")
print("1.4", type(myTuple), myTuple)
print("1.4", type(res), res)


# 1.5 Iteration through tuple 
print("1.5", "Tuple element iteration")
for i in myTuple:
    print(i)


# 1.6 Checking if element in the Tuple 
print("1.6", "Check if element in tuple")
print("Alex" in myTuple)


# 1.7 Check the lenth of a tuple
# Create tuple with a letters with it 
print("Lenght of a tuple")
lTuple = tuple("tupple")
print("1.7", len(lTuple))


# 1.8 Count specified elements in tuple 
print("Specified element coutn in a tuple")
print("1.8", lTuple.count("p"))


# 1.9 First index of specified element 
print("First index of element")
print("1.9", lTuple.index("p"))
# if element not in a Tuple -> ValueError will occur 

# 1.10 Converting tuple to list and back 
myTuple = tuple("hello")
print("Convertion from a tuple to a list")
print("1.10", "This is a tuple", type(myTuple), myTuple)
myList = list(myTuple)
print("1.10", "This is aconverted list", type(myList) , myList)


# 1.11 Slicing tuple works as slicing in list
print("Slicing tuple")
myTuple = tuple("slicing example")
# a = myTuple[start:stop:step]
print("1.11","Original tuple", myTuple)
a = myTuple[2:10:2]
print("1.11", "Slicing rule [2:10:2]", a)


# 1.12 Unpacking tuple 
print("Unpacking tuple by elements")
tupleOrg = ("Alex", 39, "Riga")
# number of variables elements, must match number of elements in a tuple! 
name, age, city = tupleOrg
print("1.12", "Original tuple :", tupleOrg)
print("1.12", "name: ", name)
print("1.12", "age: ", age)
print("1.12", "city: ", city)


# 1.13 Unpacking multiple elements using *
numTuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)
first, second, third, *rest = numTuple
print("1.13", "Original tuple", numTuple)
print("1.13", "Unpacking first:", first)
print("1.13", "Unpackind second", second)
print("1.13", "Unpacking third", third)
print("1.13", "Unpacking rest numbers", rest)
# After unpacking , tuple will be convertet to the List





"""
class tuple(object)
    tuple(iterable=(), /)

Built-in immutable sequence.
 |
 |  If no argument is given, the constructor returns an empty tuple.
 |  If iterable is specified the tuple is initialized from iterable's items.
 |
 |  If the argument is a tuple, the return value is the same object.


- count(self, value, /)
    Return number of occurrences of value.

- index(self, value, start=0, stop=9223372036854775807, /)
    Return first index of value.
    Raises ValueError if the value is not present.

"""
