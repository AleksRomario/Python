#!/usr/bin/env python3

# Создание dictionary 
d = {"house": "дом", "car": "машина", "tree": "дерево", "road": "дорога", "river":"река"}
# Обращение к элементу по ключу
print(d["house"])

# Keys уникальны в dictionary, при записи двух одинаковых key, 
# первый будет перезаписан последующим
d2 = {"key1":"one", "key1":"two", "key2":"three", "key2":"four"}
print(d2)
print(d2["key1"])
print(d2["key2"])

# Словарь можно определить с помощью функции-конструктора dict:
# Работакт только в случае если ключи являются строками str
d3 = dict(house = "дом", car = "машина", tree = "дерево", road = "дорога")
# Такой способ применяется для создания словаря на основе list
lst = [[2, "bad"], [3, "average"], [4, "good"]]
d4 = dict(lst)
print(d4)

# Формирование словаря где ключами являются элементы списка 
d5 = dict.fromkeys(["+7", "+6", "+5", "+8"])
print(d5)

# Формироварие словаря с default значением 
d6 = dict.fromkeys(["vw", "volvo","bmw", "mercedes"], "car")
print(d6)

# создание пустого списка 
d7 = {}
d8 = dict()
print(d7)
print(d8)

# Создание словаря с неизменяемыми типами:
d9 = {}
d9[True] = "Истина"
d9[False] = "Ложь"
print(d9)

# пример создания с int 
d10 = {1: "1", 2: "2"}
print(d10)

# через конструктор создание ключей с int не возможно
# d11 = dict(1 : "1", 2 : "2")

# Значения словаря могут быть любыми , а ключами только неизменяемые типы
d9["my_lst"] = [1, 2, 3]
d9[5] = 5
print(d9)

# Для удаления ключа и его значением используем del
del d9[True]
print(d9)

# При удалении несуществующего ключа , будет выведена ошибка 
# Перед удалением следует проверять наличие ключа в словаре
if 5 in d9:
    del d9[5]
print(d9)

# Как для любой коллекции можно определить длинну 
print(len(d9))
# и пройтись по каждому элементу
for key in d9:
    print(key, d9[key])
 


print('Задача 1:')
# пользователь вводит произвольные целык числа и нужно создать словарь, у которого ключами будут только четные числа, а значениями - квадраты этих чисел  
print('Задача 2:')
# Пусть имеется вот такая строка: "int = целое числоб dict = словарь, list = список, str = строка, bool = булевый тип"
# Требуется из строки создать словарь с ключами: int, dict, list, str, bool
# и соответствующими значениями
print('Задача 3:')
# Пользователь вводит с клавиатуры M раз даные в формате: английское слово: перевод1, перевод2,....,  переводN
# каждую введенную строку необходимо преобразовать и поместить в словарь, у котрого ключем будет английское слово,
# а значение список: перевод1, перевод2,...., переводN
