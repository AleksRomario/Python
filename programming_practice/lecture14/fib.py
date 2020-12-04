#!/usr/bin/env python3

# функция фиббоначи (для дальнейшего тестирования через модуль)
# С примером тестирования через документ строку 
# Тестироваться будет в случае запуска как главный модуль
# В случае если будет найдена ошибка, то будет выведена в консоль
# В противном случае пройдет тест без какого либо выводаю 

def fib(n):
	"""
	Вычисляет число Фибоначи номер n.
	Выбрасывает искоючение TypeError, если вызвына не для целочисленного типа.
	Выбрасывает исключение ValueError, если число отрицательное или больше достигнутого
	по контракту.
	:param n: целое число от 0 до 999
	:return: целое число от 0 до ...

	>>> fib(1)
	1
	>>> fib(2)
	1
	>>> fib(3)
	2
	>>> fib(4)
	6
	>>> fib(5)
	5
	"""

	if not isinstance(n, int):
		raise TypeError("Fibonacci function can work only with <class 'int'> type.")

	if n < 0:
		raise ValueError("Fibonacci can't work with negative number")

	if n >= 20:
		raise ValueError("Fibonacci can't work with numbers more than 1000")

	if n < 2:
		return n
	else:
		return fib(n - 1) + fib(n - 2)


# При запуске как главный модуль, подключаем doctect (для тестирования документ строки).
if __name__ == "__main__":
	import doctest

	doctest.testmod()
