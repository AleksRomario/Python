#!/usr/bin/env python3

# tuple - упорядоченная неизменяемая коллекция произвольных данных
# Создание 
a = 1, 2, 3, 4
print("a =", a, type(a))
b = (1, 2)
print("b = ", b, type(b))
c = 1, # присвоение одного элемента кортежа , должно заканчиваться (,) 
print("c = ", c, type(c))
print("Длинна с =", len(c))

# Присвоение значения из кортежа
# Значение в кортеже должно совпадать с переменными
x, y = (1, 2)
print("x =", x, type(x))
print("y =", y, type(y))

x1 , y1 = 1, 2

print("x1 = ", x1, type(x1))
print("y1 =", y1, type(y1))

# Доступ к кортеду осужествляется так же как и к списку
print("первый элемент кортежа а =", a[0])
print("последний элемент кортежа а =", a[-1])
# доступ через срезы
print("все элемент кортежа а =", a[0:len(a)])
print(a[:])

# Данная запись не копирует кортеж а будет ссылаться на один и тот же кортеж
d = c[:]
print(id(d), id(c))

# Кортеж не изменяемый по сравнению со списком 
# можно использовать как значение в dict что бы запретить его изменение
# кортеж занимает меньше места чем список
lst=[1,2,3]
t = (1,2,3)
print("Размер списка", lst.__sizeof__())
print("Размер кортежа", t.__sizeof__())

# создание пустого кортежа 
a1 = ()
a2 = tuple()
print(type(a1), type(a2))

# Кортеж , не изменяемый тип. Это означает что уже созданное значение мы не можем поменять
# Но добавить значение мы можем в него 
# добавление в конец
a1 = a1 + (1, 2, 3)
print(type(a1), a1)
# добавление в начало
a1 = (0,) + a1
print(type(a1), a1)
# Допускается так же добавление вложенного кортежа 
a1 = a1 +((5, 6, 7),)
print(type(a1), a1)

# допускается так же делать дублирование в кортеже 
b1 = (1, ) * 10
print(type(b1), b1)
b1 += ("hello",) * 2
print(type(b1), b1)

# Есть так же возможность создания на основе любых упорядоченных списков 
a2 = tuple([1, 2, 3])
a3 = tuple("hello world")
a4 = tuple(("hello"," world"))
a5 = tuple(("world","hello"))
print("a3 =", a3, type(a3) )
print("a4 =", a4, type(a4))
print("a5 =", a5, type(a5))

# так же из кортежа так же можно сформировать обратно список
my_new_list = list(a3)
print("my_new_list =", my_new_list, type(my_new_list))

# Кортеж может иметь различные данные внутри
a6 = (True, [1,2,3], "hello", 5, {"house": "дом"})
print(a6)
# не изменяемость относится к его структуре но не данным внутри:
# так как 1 элемент это список то мы так же можем его изменить обративнись пр индексу
a6[1].append(4)
print(a6)
# Удалить какой то конкретный элемент не возможно обратившись к нему по индексу , но можно удалить весь кортеж целиком 
del a6

# Методы кортежа 

d = ("abc", 2, [1,2], True, 2, 5)
# возвращает число найденных элементов
print(d)
print("abc =", d.count("abc"))
print("двоек =", d.count(2))

# возвращает индекс первого найденного элеметна поиска. 
# Не обязательные параметры 2 и 3 означают с какого индекса и до какого необходимо искать. 
print("длинна: ", len(d))
print("двойка идет под интексом: ", d.index(2))
print("другая двойка под интексом: ", d.index(2, 2, len(d)))
# вызовет ошибку если при поиске значения его нет в кортже
# print("двойки нет в промежутке: ", d.index(2, 3, 4))


# задание для самопроверки 

print("Задача 1")
# Дан кортеж:
# p = ("+792345678", "+792345478", "+792355678", "+592345678", "+392345678", "+7923456558")
# Нужно вывести все номера, начинающиеся с «+7».


print("Задача 2")
# Имеется набор оценок в виде строки:
# "Оценки: 5, 4, 3, 4, 2, 4, 5, 4"
# Необходимо создать кортеж, в котором находились бы только оценки в виде целых чисел:
# (5, 4, 3, 4, 2, 4, 5, 4)

print("Задача 3")
# Вывести значения кортежа:
# ((1,2,3),(3,4,5),(6,7,8))
# в виде таблицы:
# 1 – 2 – 3
# 4 – 5 – 6
# 7 – 8 – 9
