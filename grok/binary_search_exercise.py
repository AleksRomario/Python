# Grok the algorithms. Chapter 1
# Exercise 1, binary search

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
my_list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
             30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]


def binary_search(a: list, search_number: int):
    print('****')
    lower_boarder = 0
    higher_boarder = len(a) - 1

    while lower_boarder <= higher_boarder:
        middle_point = (lower_boarder + higher_boarder) // 2
        guess_number = a[middle_point]
        if guess_number == search_number:
            print('Your number is found in the list:', guess_number)
            return
        if guess_number < search_number:
            lower_boarder = middle_point + 1
        else:
            higher_boarder = middle_point - 1
    print('Your number is NOT found in the list:', search_number)
    return None


binary_search(my_list, 16)
binary_search(my_list_2, 17)
binary_search(my_list_2, -6)
