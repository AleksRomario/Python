#!/usr/bin/env python3
# Based on freeCodeCamp.org video tutorial - Intermediate Python Programming Course


# Set: unordered, mutable, no duplicate

print("1.1 Create set")
s = {1, 2, 4, 3, 5, 6, 1, 1, 1, 2, 8, 7}
# set do not contain duplicates 
print("a. Created set: ", type(s), s)
print("\n")


print("1.2 Create set with function set()")
s  = set([1, 2, 3, 4, 5])
s1 = set()
print("a. Created set given iterrable", type(s), s)
print("b. Created set w/o parameters (empty set)", type(s1), s1)
print("\n")


print("1.3 Adding to set")
print("a. Set before adding elemens", type(s1), s1)
s1.add(1)
s1.add(2)
s1.add("3")
print("b. Set after element addition", type(s1), s1)
print("\n")


print("1.4 Remove from the set using remove function()")
print("a. Set before removing elemens", type(s1), s1)
s1.remove(2)
# Removing non existing element will raise KeyError
# s1.remove(4)
print("b. Set after element removal", type(s1), s1)
print("\n")


print("1.5 Remove from the set using discard function()")
print("c. Set before removing elemens", type(s1), s1)
s1.add(6)
# will not raise error with non existing element as function parametre
s1.discard(4)
print("d. Set after element removal", type(s1), s1)
print("\n")


print("1.6 Empty our set with clear function()")
print("a. Set before element removal through clear()", type(s1), s1)
s1.clear()
print("b. Set after element removal", type(s1), s1)
print("\n")


print("1.7 Taking element by using pop function()")
s1 = set([1, 2, 2, 3, 4, 5, 6, 7, 8, 9])
print("a. Created Set before element removal using pop(): ", type(s1), s1)
r = s1.pop()
print("b. Set after poping element: ", type(s1), s1)
print("c. Poped element: ", type(r), r)
print("\n")


print("1.8 Iteration of the loop")
for i in s1:
    print(i)
print("\n")


print("1.9 Check if value is in Set")
if 2 in s1:
    print("a. Yes value is in set")
else:
    print("b. Not value is not in Set")
print("\n")


print("1.10 Set - Union and intersections")
# Do not modify original sets.
odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

# Union - combination of both sets without duplication 
union = odds.union(evens)
print("a. Union odds and evens result: ", union)
print("\n")

# Intersection - takes only elements found in both elements
print("1.11 Intersections of two Sets")
# Do not modify original sets.
intersection = evens.intersection(primes)
print("a. intersection of evens and primes", type(intersection), intersection)
print("\n")


# Diference  - return a set. All element from setA that non in setB
print("1.12 - Diference of two Sets")
# Do not modify original sets.
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}
print("SetA", setA)
print("SetB", setB)
diff =setA.difference(setB) 
print("Difference of setA and setB: elements from setA that not in setB", diff)
diff2 =setB.difference(setA) 
print("Difference of setB and setA: elements from setB that not in setA", diff2)
print("\n")



print("1.13 Symmetric difference method - return from setA and setB elements than not in the set")
# Do not modify original sets.
diff2 = setA.symmetric_difference(setB)
print("Symmetric difference of setA from setB", diff2)
diff3 = setB.symmetric_difference(setA)
print("Symmetric difference of setB from setA", diff3)
diff3 = setA.symmetric_difference(setB)
print("\n")


print("1.14 Update - adds the elements to setA from setB that was not exist")
# Will modify setA 
print("Original setA before update with setB", setA )
setA.update(setB)
print("SetA after update with setB:", setA)
print("\n")



print("1.15 Intersection Update")
print("\n")




"""
print("1.12 X")
print("\n")
print("1.12 X")
print("\n")
"""



"""
class set(object)
 |  set() -> new empty set object
 |  set(iterable) -> new set object
 |
 |  Build an unordered collection of unique elements.
 |
 |  Methods defined here:
 add(...)
 |      Add an element to a set.
 |
 |      This has no effect if the element is already present.
 |
 |  clear(...)
 |      Remove all elements from this set.
 |
 |  copy(...)
 |      Return a shallow copy of a set.
 |
 |  difference(...)
 |      Return the difference of two or more sets as a new set.
 |
 |      (i.e. all elements that are in this set but not the others.)
 |
 |  difference_update(...)
 |      Remove all elements of another set from this set.
 |
 |  discard(...)
 |      Remove an element from a set if it is a member.
 |
 |      If the element is not a member, do nothing.
 |
 |  intersection(...)
 |      Return the intersection of two sets as a new set.
 |
 |      (i.e. all elements that are in both sets.)
 |
 |  intersection_update(...)
 |      Update a set with the intersection of itself and another.
 |
 |  isdisjoint(...)
 |      Return True if two sets have a null intersection.
 |
 |  issubset(...)
 |      Report whether another set contains this set.
 |
 |  issuperset(...)
 |      Report whether this set contains another set.
 |
 |  pop(...)
 |      Remove and return an arbitrary set element.
 |      Raises KeyError if the set is empty.
 |
 | remove(...)
 |      Remove an element from a set; it must be a member.
 |
 |      If the element is not a member, raise a KeyError.
 |
 |  symmetric_difference(...)
 |      Return the symmetric difference of two sets as a new set.
 |
 |      (i.e. all elements that are in exactly one of the sets.)
 |
 |  symmetric_difference_update(...)
 |      Update a set with the symmetric difference of itself and another.
 |
 |  union(...)
 |      Return the union of sets as a new set.
 |
 |      (i.e. all elements that are in either set.)
 |
 |  update(...)
 |      Update a set with the union of itself and others."""
