#!/usr/bin/env python3
print("--- Создание и импорт модулей ---")

# ренне осуществлялся импорт модулей для расширения функциональности языка
# указывая import и далее указание имени модуля: 
# import <название модуля>
# Возможно подключение модулей через запятую:
# import <название модуля>, <название модуля>, <название модуля>
# Подкоючив модуль, получаем доступ к функциям модуля:
# <название модуля>.<название функции>

print("\n")
print("--- Вызов функции стороннего модуля ---")

import math
res = math.cos(0.7)
print("результат функции math.cos: ", res)


print("\n")
print("--- Вызов функции собственного  модуля ---")

# пример подключения собственного модуля mymath
# при импорте образуется пространство имен модуля mymath
import mymath
m = mymath.sum(1, 4)
print("Результат сложения (из собственного модуля): ", m)
print("Переменная из собственного модуля: PI =", mymath.PI)

print("\n")
print("--- Пример подключения и вызов опредленной функции ---")
# В случае если нехочется создавать новое пространство имен, то можно
# импортировать по правилу: 
from mymath import max3
# в этом случае будет доступна только указанная функция
# для её вызова не требуется использовать пространство имен (имя модуля)
# при необходимости импорта нескольких функциц они перечисляются 
# через зарятую
# Для получения всего содержимого используется (*), при этом может 
# появится конфликт с уже существующими функциями 

print("\n")
print("--- Пример импортирования через алиас ---")

from math import max2 as my_max
m = my_max(10, 5)


# Задания для самоподготовки

#1. Создайте модуль с двумя функциями, которые бы вычисляли периметр и 
# площадь прямоугольника. Подключите этот модуль к основной программе и 
# вызовите эти функции с аргументами, введенные с клавиатуры.

# 2. Задайте в модуле словарь, в котором ключами являются английские 
# слова, а значениями соответствующие русские (переводы). Также добавьте 
# необходимые функции для добавления и удаления новых слов в этом словаре. 
# Импортируйте этот модуль в основную программу и реализуйте мини-словарь 
# со следующим меню (функционалом):

#1. Перевести слово
#2. Добавить слово
#3. Удалить слово
#4. Завершить работу

# Попробуйте развить идею словаря и добавьте возможность автоматического сохранения и считывания данных из файла (в файле сохраняется словарь целиком).

# m3 = max3(1, 5, 4)
# print("Максимальное значение из введенных переменных: ", m3)


