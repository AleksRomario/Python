#!/usr/bin/env python3

# set - это неупорядоченная коллекция уникальных элементов
# В которых отсутствуют дублирующие значения 

# создание множества 
s = {1, 2, 3, 4, 5}
print(s, type(s))

# при повторении значений в set они игнорируются 
s1 = {1, 2, 3, 4, 5, 1, 3, 5 , 6, 7, 7, 8, 9}
print(s1, type(s1))

# В качестве значений любой неизменяемый тип: числа, строки, кортежи
s2 = {1, 1, "hello", "hello", ("a", "b"), ("a", "b"), 2}
print(s2, type(s2))

# Создание set с помощью фукнции set:
s3 = set()
# или с указанием любого итерируемого объекта:
s4 = set("hello world")
print(s3, type(s3))
print(s4, type(s4))

# Возможно даже создание с функцией range:
s5 = set(range(10))
print(s5, type(s5))

# При создании s6 = {} получим не set, а dict. 
# Поэтому создавать надо через функцию для пустого set: как s3
s6 = {}
print(s6, type(s6))

# Используется для удаления всех посторений в list 
# Для этого из list->set а потом из set->list
l = [1, 2, 3, 1, 3, 4, 5, 6, 5, 3, 2, 7, 6, 8, 9]
print(l, type(l))
s6 = set(l)
l = list(s6)
print(l, type(l))
# Так же можно прописать данную операцию в одну строку 
l2 = [1, 2, 3, 1, 3, 4, 5, 6, 5, 3, 2, 7, 6, 8, 9]
l2 = list(set(l2))
print(l2, type(l2))

# Элементы множества можно обходить с помощью цикла for:
s7 = {1, 4, 5, 6, 7, 9}
for x in s7:
    print(x)

# Методы добавления удаления элементов в множестве
# для добавления одного элемента используется add:
s7.add(3)

# Для добавления нескольких используется update:
# в качечтве объекта необходимо указать итерируемый объект
s7.update([2, 8])
s7.update("abrakadabra")
print(s7, type(s7))

# для удаления используется discard или remove:
s7.discard(1)
s7.remove(2)
# при удалении не существующего объекта с помощью:
# discard - не произойдет ошибка
# remove - произойдет ошибка
print(s7, type(s7))

# так же можно использовать pop(), в этом случае вернется случайный объект 
# так как set это неупорядоченный список = s7.pop()
rnd = s7.pop()
print(rnd, type(rnd))

# Для удаления всего set используктся clear():
s7.clear()
print(s7, type(s7))

