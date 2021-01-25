#!/usr/bin/env python3 

# F-строки и метод format
age=18
name="Alex"
print("My name is " + name + " I am " + str(age))

# более удобный способ использовать str.format(*args)
print("My name is {0} I am {1}" .format(name, age))

# с использованием именованых переменных 
print("My name is {age} I am {old}" .format(age=name, old=age))

# Применение F-строки
# внутри фигурных скобок можно записывать любые конструкции 
# например операции арифметические операции и операции со строками
msg = f"My name is {name} I am {age}"
print(msg)
msg1 = f"My name is {name.upper()} I am {age + 20}"
print(msg1)

# Задание для самоподготовки

# 1. Пользователь через пробел вводит ФИО. На основе этой информации требуется создать строку с сообщением:

# Ваши персональные данные: 
# Фамилия: введенная фамилия 
# Имя: введенное имя 
# Отчество: введенное отчество

# 2. Имеется текстовый файл с содержимым:

# Иван, ivan@gm.com, 18 
# Татьяна, tat@gm.com, 22 
# Сергей, srg@ml.ru, 33 
# Федор, fr@ml.ru, 41 
# Елена, el@gm.com, 27

# Необходимо построчно считывать информацию и для каждой строки для лиц не старше 30 лет сформировать сообщение:

#Уважаемый(ая) <имя>! Приглашаем Вас принять участие в курсах по изучению Python. Подробную информацию мы выслали на email: <email>.
