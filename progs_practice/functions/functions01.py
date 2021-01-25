#!/usr/bin/env python3

# простая функция не принимающая параметров, выводит в консоль текст
def say_hello():
    print("hello")

say_hello()
print(type(say_hello))
f = say_hello
f()

# Функция принимающая несколько значений 
def add_numbers(x, y):
    return x + y 

number_sum = add_numbers(5, 6)
print(number_sum)

# Функция с формальными параметрами
# формальные параметры необходимо записывать последними иначе ошибка
def say_hi(msg, end="!"):
    print(msg + end)

say_hi("hi")
say_hi("hello again", "!!!")

# при указывании нескольких формальных параметров можно передавать значение
# только для конкретного параметра. В таком случае такой параметр будет 
# называться именованным (передача параметра с указанием имени параметра).

def name_param(msg, end="!!!", sep=":"):
    print(msg + sep + end)

name_param("hello", end="-")

# При необходимости возврата нескольких параметров используется конструкция:
def perAndSq(w, h):
     res =  2*(w+h), w*h
     print(res)
# Результатом будет кортеж с вычислениями 
perAndSq(6, 7)

# возможно и присвоение кортежем:
def perAndSq2(w, h):
     per, sq2 =  2*(w+h), w*h
     print("периметр: ",per)
     print("квадрат: ",sq2)

perAndSq2(6, 7)

# Функция возведение числа в целую степень: 
def myPow(x, n):
    sx = 1
    while n>0:
        sx = sx * x 
        n = n - 1
    return sx

print(myPow(2, 3))

# Задания для самоподготовки

# 1. Задайте и вызовите функцию, которая вычисляет площадь прямоугольника.
 
def rectangle_area(a, b):
    return a * b

print(f"Площадь прямоугольника: {rectangle_area(3, 5)}")

# 2. Необходимо создать функцию, которая в зависимости от значения формального параметра type будет вычислять или площадь или периметр прямоугольника.

FORMAL = False 

if FORMAL:
    def rectangle(a, b):
        return (a + b) * 2
else:
    def rectangle(a, b):
         return a * b

print(rectangle(5, 6))

# 3. Написать функцию поиска максимального значения из переданного ей списка значений.

numbers = []

def find_max(*args):
    pass

print(find_max(numbers))

# 4. Написать функцию вычисления произведения значений элементов переданного ей списка.
