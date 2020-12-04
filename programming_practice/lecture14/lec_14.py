#!/usr/bin/env python3 

#  Пример тестирования Unittest 
import unittest


# Все необходимые тесты фломируются в один класс в виде функций 
# Проводится проверка с использованием assertTrue, assertFalse, assertEqual

# класс в данном случае является потомком класса unittest.TestCase  
class TestStringMethods(unittest.TestCase):

    # начало название функций обязательно начинается с test_, это определяет автоматический запуск проверки. Другое
    # название не будет вызываться в качестве части тестового задания.

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


# При запуске как главный модуль вызывается класс Unittest и у него main()
if __name__ == '__main__':
    unittest.main()
