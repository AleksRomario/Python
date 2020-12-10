#!/usr/bin/env python3

# List comprehention 
# Разбиение на числа введенного числа пользователем 

number = int(input('Введите число для дальнейшего его разбиение на отдельные цифы: '))
separated_digits = []
# Пока number не будет равнятся 0 делаем цикл
while number: 
    # берем остаток от деления и записываем в List 
    # separated_digits.append(number % 10) 
    
    # Для запоминания в обратном порядке 
    separated_digits = [number % 10] + separated_digits
    # берем целочисленную цифру от деления на 10
    number //= 10
    # после деления последей цифры получаем 0 и заканчиваем цикл 
print(separated_digits)

'''
тест сложение двух листов 
a = []
print(a)
a = [2] + a 
print(a)
a = [1] + a 
print(a)
a = [0] + a
print(a)
'''

# Изменение порядка следования элементов в списке

list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]




