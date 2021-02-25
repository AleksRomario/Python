#!/usr/bin/env python3
"""

"""

print("--- my solution ---")

def listCounter(l):
    print(l.count(4))

listCounter([1, 2, 3, 4, 5, 6, 7, 8, 9, 4])
listCounter([1, 2, 4, 4, 4, 4, 6, 4])

print("--- w3resource solution ---")
def list_count_4(nums):
  count = 0
  for num in nums:
    if num == 4:
      count = count + 1

  return count

print(list_count_4([1, 4, 6, 7, 4]))
print(list_count_4([1, 4, 6, 4, 7, 4]))
