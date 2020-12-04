#!/usr/bin/env python3 

# подсчет букв ‘a’ в строке «abrakadabra». 
print('Задача 1:')
string = "abrakadabra"
counter = 0
for letter in range(len(string)):
	if string[letter] == "a":
		counter += 1
print("a) В слове:", string, counter, "букв 'a'!")
print("b) В слове: %s %d букв 'a'!" % (string, counter))
print(f"c) В слове: {string} {counter} букв 'a'!")


# удаление всх сочетаний «ab» в «abrakadabra»
print('Задача 2:')
string2 = "abrakadabra"
result_string2 = string2[2:7] + string2[9:11] 
print("a) При удалении всех 'ab'из слова %s получается: %s"%(string2, result_string2))

result_string2 = string2.replace('ab', '')
print("b) При удалении всех 'ab'из слова %s получается: %s"%(string2, result_string2))


# Напишите программу определения слова палиндрома (это слова, которые одинаково читаются в обоих направлениях, например, анна, abba и т.п.). Слово вводится с клавиатуры.
print('Задача 3:')
string3 = input('ввдите слово для проверки палиндрома:')
string_reversed3 = string3[::-1]
if string3 == string_reversed3: 
	result_string3 = 'является'
else:
	result_string3 = 'не является'
print('Введенное слово %s: %s полиндромным.'% (string3, result_string3))


# Напишите программу определения количества вхождений фраз «ra» в слове «abrakadabra».
print('Задача 4:')
string4 = "abrakadabra"
search4 = 'ra'
print('Входжение %s в слово %s %d раза.' %(search4,string4, string4.count('ra'))) 


#Разделите введенное с клавиатуры предложение на слова (слова разделяются пробелом).
print('Задача 5:')

string5 = input('Введите предложение для последующего разделения на слова:')
my_list = string5.split()
print(my_list)
