#!/usr/bin/env python3

print("--- Сортировка методом sort() для list ---")
# в Python присутствует довольно гибкий механизм для сортировки элементов 
# упорядоченных коллекций. Реализуется:
# встроенным методом списков (list) - sort()
# или функцией sorted для всех остальных типов коллекций 

# Отличие вызовов: 

lst = [1,2, -1, -2, 0]
print(type(lst), lst)
# свойство list
lst.sort(reverse = False)
print(type(lst), lst)
# происходит изменение текущего list

print("\n")
print("--- Сортировка функцией sorted() для остальных коллекций ---")
# предположим имеем кортежи:
myTuple = ("aa", "ac", "ab", "af", "ad")
print(type(myTuple), myTuple)
res = sorted(myTuple)
# При применении функции в итоге результытом будет list
print(type(res), res)
myTuple= tuple(res)
# переносим опять в Tuple
print(type(myTuple), myTuple)
# при применении не изменяет существующую коллекцию, а возвращает list

print("\n")
print("--- Сортировка функцией sorted() для str ---")

myStr = "hello world"
res = sorted(myStr, reverse = True)
print(type(res), res)

# оба данных подхода сортировки поддерживают необязательный парамето 
# reverse = True / False 
# Который определяет порядок сортировки по возврастанию (False) - default
# или убыванию (True)


print("\n")
print("--- Своя сортирующая функция ---")
# для более точной настройки алгоритма используется собственная функция

a = [1, 4, 3, 6, 7, 5, 2]
print('Сортиртруемый список', a)
# преположим мы хотим сначала четные элементы а после нечетные элементы
# создадим функцию возвращающую 
def sortFunc(x):
    return x%2

print("--- Сортировка N2---")
print(sorted(a, key=sortFunc))
# при вызове возвращается либо 1 либо 0 по этим параметрам и будет 
# происходить сортировка 

# в итоге будет отсортированы  сначала не четные, после четные
# но сами значения четных не будут отсортированы 
# для сортировки самих четных или не четных значения необходимо 
# переопределить собственную функциию 

def sortFuncPro(x):
    if x%2 == 0:
        return x
    else:
        return x + 100

# в функции если число четное вернуть его без изменений , если не четное 
# то вернуть его прибавив 100
# таким образом будут сначала сортироваться четные значения такие как 
# они есть 
# после четных будуи сортироваться не четные значения 
# работать это будет только в том случае если числа для сортировки будут 
# не более 99 

print("\n")
print("--- Сортировка N2---")
print(sorted(a, key=sortFuncPro))

print("\n")
cities = ["Riga", "London", "Moscow", "Rio"]

print("--- Сортировка N3---")
print("Сортирируемый список", cities) 

# применим сортировку исходя из длинны строк
print(sorted(cities, key=len))


print("\n")
print("--- Сортировка N4---")
print("Сортировка по первому символу") 
print(sorted(cities, key = lambda x: x[0]))
print("Сортировка по последнему символу")
print(sorted(cities, key= lambda x: x[-1]))


# Задания для самоподготовки

# 1. Используя сортировку, найдите первые три наименьшие значения в списке:
# a=[1,2,-5,0,5,10]
# Сам список должен оставаться неизменным.

# 2. Отсортируйте список:
# digs = (-10, 0, 7, -2, 3, 6, -8)
# так, чтобы сначала шли отрицательные числа, а затем, положительные.

#3. Пусть имеется словарь:
# {'+7': 2345678901, '+4': 3456789012, '+5': 5678901234, '+12': 78901234}
#Необходимо вывести телефонные номера по убыванию чисел, указанных в 
# ключах, то есть, в порядке:
# +4, +5, +7, +12
