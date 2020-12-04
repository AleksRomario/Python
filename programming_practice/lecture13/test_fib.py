#!/usr/bin/env python3
import fib

# Пример тестового файла для тестирования fib.fib()  
# подключаеься для тестирования определенного модуля
# Скрипт написан таким образов, что бы проверять пары и в случае ошибки вывести эту пару.


#final_correct = final_correct & correct    <=  equals   =>    final_correct &= correct
# Изначально фиксирукс флаг True у финального результа
all_correct  = True
for n, answer in [(0, 0), (1, 1), (2, 2), (5, 10)]:
	result = fib.fib(n)	
	correct = result  == answer
	if not correct: 
		print('Faulure', n , answer, "Ответ должен быть: ", result)
	all_correct &= correct

# Проверяем финальный результат для вывода коректного сообщения 
if all_correct:
	print("Testing fib: OK")
else: 
	print("Testing fib: Fail")

