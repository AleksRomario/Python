#!/usr/bin/env python3

# Input from keyboard and print on screen. 
# Для того что бы переменную можно было поместить в текст примеянтся сначала
# f(сокращённое от functional). Пример идет далее 
separator = "--------------------------------------"
print(separator)
name =input("What is your name? ")
print(f"Hello, {name}" )

print(separator)

# Пример вветления программы 
x = int(input("Сколько циклов необходимо? "))
# пример бесконечного цикла 
while True:
	x -= 1 
	# Условие при котором закончить программу
	if x <= 0:
		print(f"Count down finished with x = {x}")
		break
	print(f"Current x is {x}")
print("DONE")

print(separator)

# Последовательность цикла for для чисел 2, 3, 4, 5 
for x in 2, 3, 4, 5:
	print(x**2)

print(separator)

# Применение арифметической последоватьльности с помощью генерации
# range(start, stop, step)
for x in range(5, 1, -1):
	print(x**2)

print(separator)

