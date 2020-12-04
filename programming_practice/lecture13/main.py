#!/usr/bin/env python3

# Главная для получения доступа к функции fib.py для расчета числа фибаначчи 

import fib

def main():
	n = int(input("Введите номер числа Фиббаначи: "))
	f = fib.fib(n)
	print(f)
	
if __name__ == "__main__":
	main()
