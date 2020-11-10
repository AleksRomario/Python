# Grock the algorythms. Chapter 2 
# Exercise 2, selection sort O(n*n)
# need to test it (not finished script)



# find the smallest in array 
def find Smallest(arr):
    # for smallest value 
    smallest = arr[0]
    # for smallest index of value 
    smallest_index = 0
    for i in range(l, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

#selection sort
#looking in array looking for smallest value and copying it value to the new array 
def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = indSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

print selectionSort([5, З, 6, 2, 10])
