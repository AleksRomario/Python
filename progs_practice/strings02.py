#!/usr/bin/env python3

# Основные методы строк
# Проверка корректности ввода тел. номера по шаблону: x(xxx)xxxxxx
print('Задача 1:')

def some_entry(entry):
	if entry.isdigit():
		print('Digit\' accepted!')
	else:
		print('Entry error!')


some_entry('1234123456')
#some_entry('54666g33t6')

# Изменить строку "2+3+6.7 + 82 + 5.7 +1" в которой все «+» заменены на «-» и удалены все пробелы
print('Задача 2:')
text  = "2+3+6.7 + 82 + 5.7 +1"
text =  text.replace('+','-').replace(" ", "")  
print('Замененный результат:', text)


# Написать программу вывода чисел 0; -100; 5.6; -3 в виде столбца: в котором все строки выровнены по правому краю (подсказка: воспользуйтесь методом rjust).
print('Задача 3:')

a = str(0) 
b = str(-100)
c = str(5.6)
d = str(-3)
e = a + ";" + b+ ";" + c + ";" + d
e = e.split(';')
print("Результат вывода в столбик:") 

for i in e:
	print (i.rjust(4))


# В строке "abrakadabra" найдите все индексы подстроки «ra» и выведите их (индексы) в консоль.
print('Задача 4:')


# проверить есть ли совпадения
string = "abrakadabra"
search = "ra"
# определить индекс входжения
if (search in string):
	copies = string.count(search)
	print (copies)
	start = 0
	value = 0
	a = []
	for i in range(len(a)):

		value =  string.index(search, start + value ) 
		start = start + 1 	
		a.insert(i , value)
print(a)
# сохранить индекс для поиска следующего 
# расречатать найденные индксы






