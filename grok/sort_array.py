# Grock the algorythms. Chapter 2 
# Exercise 2, selection sort O(n*n)
# need to test it (not finished script)


# find the smallest in array
def find_smallest(arr):
    # for smallest value 
    smallest = arr[0]
    # for smallest index of value 
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


# selection sort
# looking in array looking for smallest value and copying it value to the new array
def selection_sort(arr: list) -> list:
    new_arr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr


print(selection_sort([5, 3, 6, 2, 10]))
