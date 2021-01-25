#!/usr/bin/env python3
print("Функции-генераторы")

# вычисляет средние арифметические для каждой из сумм: для одного 
# значения, для двух, трех и так до N

def getAllAverage(N):
    avs = []
    count = 0
    S = 0
    for i in range(1,N+1):
        count += 1
        S += i
        avs.append( S/count )
 
    return avs

print(getAllAverage(100))
print(getAllAverage(100).__sizeof__())

# функция генертор:
# оператор yield возвращает значение x и замораживает текущее состояние 
# функции. В результате, при ее повторном вызове цикл for начнется не 
# с начала, а с той итерации, на которой был заморожен, то есть, перейдет 
# к следующему значению x и оператор yield возвратит следующее значение.

def f():
    for x in range(10):
        yield x

s = f()
print(s)

# next() - Итератор – это объект, который поддерживает функцию next() 
# для перехода к следующему элементу коллекции.

print(next(s))
print(next(s))
print(next(s))
print(next(s))

def getAllAverage2(N):
    count = 0
    S = 0
    for i in range(1,N+1):
        count += 1
        S += i
        yield S/count

it = getAllAverage2(10)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

# В результате, мы последовательно будем получать вычисленные значения, 
# не затрачивая дополнительной памяти на их хранение.


# Задание для самоподготовки
# Пусть дан текст:

# t = """Генератор – это итератор, элементы которого 
# можно перебирать (итерировать) только один раз. 
# Итератор – это объект, который поддерживает функцию next() 
# для перехода к следующему элементу коллекции."""

# Написать функцию-генератор для выделения слов из этого текста (слова 
# разделяются пробелом, либо переносом строки ‘\n’). Список всех слов 
# при этом в функции не создавать.
