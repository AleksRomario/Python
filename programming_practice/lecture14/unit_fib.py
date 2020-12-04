#!/usr/bin/env python3
# Пример тестирования Unittest на основе fib()

# Планирование набора тестов.
# TEST_SIMPLE: Простые тесты : 0 -> 0 , 1 -> 1, 2 -> 1, 3 -> 2.
# TEST_STRESS:Средние тесты (средние тесты): 50 -> , 1000000 -> . Для тестирования времени выполнения подвивисает.
# В случае огромного числа, функция должна реализовать отказ (не хватит памяти вычислить) и какого типа.
# Используем Исключения exception -> вызов ValueError
# TEST_NEGATIVE: Проверка на устойчивость: отрицательные числа: -1 -> ValueError  , -10 -> ValueError .
# TEST_WRONG_PARAM_TYPE: Не правильные параметры,  Отказ функции (исключения). 2.5 -> реакция TypeError(ValueError)

import unittest
from fib import fib

# def fib(n):
#     """
#     Вычисляет число Фибоначи номер n.
#     Выбрасывает искоючение TypeError, если вызвына не для целочисленного типа.
#     Выбрасывает исключение ValueError, если число отрицательное или больше достигнутого
#     по контракту.
#     :param n: целое число от 0 до 999
#     :return: целое число от 0 до ...
#     """
#     pass

# Все необходимые тесты фломируются в один класс в виде функций 
# Проводится проверка с использованием assertTrue, assertFalse, assertEqual
# класс в данном случае является потомком класса unittest.TestCase


class TestFibonacci(unittest.TestCase):
    # начало название функций обязательно начинается с test_,
    # это определяет автоматический запуск проверки. Другое
    # название не будет вызываться в качестве части тестового задания.

    def test_simple(self):
        for param, result in [(0, 0), (1, 1), (2, 1), (3, 2), (10, 55)]:
            self.assertEqual(fib(param), result)

    def test_stress(self):
        self.assertEqual(fib(15), fib(14) + fib(13))
        with self.assertRaises(ValueError):
            fib(20)

    def test_negative(self):
        with self.assertRaises(ValueError):
            fib(-1)
        with self.assertRaises(ValueError):
            fib(-100)

    def test_wrong_param_type(self):
        with self.assertRaises(TypeError):
            fib(5.5)
        with self.assertRaises(TypeError):
            fib('Test')


# При запуске как главный модуль вызывается класс Unittest и у него main()
if __name__ == '__main__':
    unittest.main()
