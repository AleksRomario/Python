#!/usr/bin/env python3 
import time

# реализация алгоритма Евклида для поиска наибольшего общего делителя
# выполние его тестирование с применением тестирующей функции.

def getNOD(a, b):
    """Вычисляется НОД для натуральных чисел a и b
        по алгоритму Евклида.
        Возвращает вычисленный НОД.
    """
    if a < b:
        a,b = b,a
 
    while b:
        a,b = b, a%b
 
    return a


def testNOD():
    #--- тест 1 ---
    a=28; b=35
    res = getNOD(a,b)
    if res == 7:
        print("#test1 - ok")
    else:
        print("#test1 - fail")

    #--- тест 2 ---
    a=100; b=1
    res = getNOD(a,b)
    if res == 1:
        print("#test2 - ok")
    else:
        print("#test2 - fail")

    #--- тест 3 ---
    a=2; b=10000000000

    st = time.time()
    res = getNOD(a,b)
    et = time.time()
    dt = et-st
    if res == 2 and dt < 1:
        print("#test3 - ok")
    else:
        print("#test3 - fail")

testNOD()

# Задание для самоподготовки
# 1. Реализовать последний вариант алгоритма Евклида с помощью рекурсивной
# функции.

# 2. Написать функцию нахождения максимального значения среди переданных 
# аргументов: arg1, arg2, …, argN

# 3. Реализовать универсальную функцию для нахождения максимального или
# минимального значения среди аргументов: arg1, arg2, …, argN
# с помощью функции-селектора, указанной в виде лямбда-функции
# как один параметров функции поиска.