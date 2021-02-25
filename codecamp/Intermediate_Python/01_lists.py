:#!/usr/bin/env python3
# Based on freeCodeCamp.org video tutorial - Intermediate Python Programming Course


# Lists: ordered, mutable, allows duplicate elements


# 1.1 creating list rule is: create in  [], separated by (,)
mylist = ["banana", "cherry", "apple"]
print(1.1, mylist)


# 1.2 Can be created empty list using dunction 
mylist2 = list()
print(1.2, mylist2)


# 1.3 List can contain diferent data types (duplicates allowed) 
mylist3 = [5, True, "Yes", (1, 2), "Yes"]
print(1.3, mylist3)


# 1.4 If you want access the element of the list, you refering to it by index
item = mylist[0]
print(1.4, item)


# 1.5 Negative index refers to the last item (do not put index oit ir range)
item = mylist[-1]
print(1.5, item)


# 1.6 Iteration through the list: using for loop
print(1.6)
for i in mylist:
    pass  #  do something - like print all the entities - print(i)
    print(i)


# 1.7 Checking if the item in the list 
if "banana" in mylist:
    print(1.7, "Yes")
else:
    print(1.7, "No")


# 1.8 Checking how many elemets in you list 
lenght = len(mylist)
print(1.8, lenght)


# 1.9 append items to the list (inserts as last element of the list)
mylist.append("apple")
print(1.9, mylist)
# print the methods of the list
#print(dir(mylist))


# 1.10 Insert item to the list (need to specify which index to insert to)
mylist.insert(1, "lemon")
print("1.10", mylist)


# 1.11 Remove specific element from the list (need to specify only item name)
# ValueError ocur if you removing non existing element from the list
mylist.remove("apple")
# removed apple from the list (first occurrence)
print(1.11, mylist)


# 1.12 Remove - pop will remove and return item at the specified index, last by default. 
removed_via_pop =  mylist.pop()
print(1.12, mylist)
#print(removed_via_pop)


# 1.13 Clear the list
#mynewlist = mylist
#mynewlist.clear()
#print(1.13, mynewlist)


# 1.14 Reverse the items in the list
mylist.reverse()
print(1.14, mylist)


# 1.15 Sorting list
# Do not change original list
sortedlist = sorted(mylist)
print(1.15,"sortedlist = serted(list)",  sortedlist)
print(1.15, "Before mylist.sort()", mylist)
# Changes list that was sorted whith method 
mylist.sort()
print(1.15, "mylist.sort()",  mylist)


# 1.16 Simple way to Create new list filled with some data 
numbersList = [0] * 10
print(1.16, "Creates list of zeroes", numbersList)


# 1.17 It is the posibility to concatinate the lists 
listOne = [1, 2, 3]
listTwo = [4, 5, 6]
res = listOne + listTwo
print(1.17, "listOne", listOne)
print(1.17, "listTwo", listTwo)
print(1.17, "Result of listOne + listTwo", res)

# 1.18 Slicing the list

slicingList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a = slicingList[1:7:2]
# [begining:end:step]
# if begining not specified - starts from beginig
# if ending not specified - ends after last element
# step reprpesents hwitsh element to show . if 2 - every second. if -1 - reverse order
print(1.18, "Slicing list", slicingList)
print(1.18, "Slicing [1:7:2] result", a)

# 1.19 To Copy 
# If you use simple assignment two lists will refers to the same memory address
list_org = [1, 2, 3]
list_cpy = list_org
list_cpy.append(4)
print(1.19, "Simple assignment")
print(1.19, "Original List", list_org)
print(1.19, "Copy List + append", list_cpy)
print(1.19, "Using copy() method")
list_cpy = list_org.copy()
list_cpy.append(5)
print(1.19, "Original List", list_org)
print(1.19, "Copy List + append", list_cpy)
# Actual copy can be done with list() function, passing original as argument
list_cpy = list(list_org)
print(1.19, "Assignment with list()")
list_cpy.append(5)
print(1.19, "Original List", list_org)
print(1.19, "Copy List + append", list_cpy)
# Additional copy can be made by slicing
print(1.19, "Assignment with list()")
list_cpy = list_org[:]
list_cpy.append(5)
print(1.19, "Original List", list_org)
print(1.19, "Copy List + append", list_cpy)

# 1.20 List Comprehension 
# Creating new list from existing list
aList = [1, 2, 3, 4, 5, 6, 7]
bList = [i*i for i in aList]
print("1.20", "Original list", aList)
print("1.20", "List made by using List Comprehension", bList)


"""
Methods of the list (man list)

- append(self, object, /)
      Append object to the end of the list.

- clear(self, /) 
    Remove all items from list.

- copy(self, /) 
    Return a shallow copy of the list.

- count(self, value, /)
    Return number of occurrences of value.

- extend(self, iterable, /)
    Extend list by appending elements from the iterable.

- index(self, value, start=0, stop=9223372036854775807, /)
    Return first index of value.
    Raises ValueError if the value is not present.

- insert(self, index, object, /)
    Insert object before index.

- pop(self, index=-1, /)
    Remove and return item at index (default last).    
    Raises IndexError if list is empty or index is out of range.

- remove(self, value, /)
    Remove first occurrence of value.    
    Raises ValueError if the value is not present.

- reverse(self, /)
    Reverse *IN PLACE*

sort(self, /, *, key=None, reverse=False)
    Sort the list in ascending order and return None.    
    The sort is in-place (i.e. the list itself is modified) and stable (i.e. the
    order of two equal elements is maintained).  
    If a key function is given, apply it once to each list item and sort them,
    ascending or descending, according to their function values.    
    The reverse flag can be set to sort in descending order.


"""
