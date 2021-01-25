#!/usr/bin/env python3 


# Дан список [-1, 0, 5, 3, 2]. Необходимо изменить его, увеличив каждое значение на 7.2. 
print('Задача 1:')

test_list = [-1, 0, 5, 3, 2]
for x in range(len(test_list)):
    test_list[x] *= 7.2
print(test_list)

# С использованием list comprehensions 

test_list2 = [-1, 0, 5, 3, 2]
test_list2 = [test_list2[x] * 7.2 for x in range(len(test_list2))]
print(test_list2)

# Пользователь вводит с клавиатуры N значений (строки или числа). На их основе сформировать список, состоящий из продублированных элементов. (Например, из значений 1, 5, "abc" формируется список [1, 1, 5, 5, "abc", "abc"]).
print('Задача 2:')

#input('Введите значения:')

#Написать программу сложения двух матриц:
#     
#     |1 2| |1 0|
#  A =|3 4|+|0 1|  
#     |5 6| |1 1|
#
print('Задача 3:')

matrix_1 = [1, 2, 3, 4, 5, 6]
matrix_2 = [1, 0, 0, 1, 1, 1]
common_matrix = [] * len(matrix_1)
common_matrix = [matrix_1[x] + matrix_2[x] for x in range(len(matrix_1))]
print(common_matrix) 

# Пользователь вводит N значений в список. Необходимо проверить: было ли введено число 5.
print('Задача 4:')


