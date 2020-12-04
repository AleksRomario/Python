#!/usr/bin/env python3

# функция фиббоначи (для дальнейшего тестирования через модуль)
# С примером тестирования через документ строку 
# Тестироваться будет в случае запуска как главный модуль
# В случае если будет найдена ошибка, то будет выведена в консоль
# В противном случае пройдет тест без какого либо выводаю 

def fib(n):
	"""
	This is the "example" module.

	The example module supplies one function, fib().  For example,

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

	if n < 2:
		return n
	else:
		return fib(n-1) + fib(n-2)

# При запуске как главный модуль, подключаем doctect (для тестирования документ строки).
if __name__ == "__main__":
	import doctest
	doctest.testmod()
