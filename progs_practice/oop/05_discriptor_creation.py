#!/usr/bin/env python3
print("--- Создание дискрипторов классов ---")

# При создании объектов свойств необходимо определять однотипные объекты
# Для избежания этого пользуются механизмом дискриптеров

# Дискпиптор - это класс в котором определены следующие специальные методы:

class CoordValue:
    def __get__(self, instance, owner):
        return self.__value

    def __set__(self, instance, value):
        self.__value = value 

    def __delete__(self, obj):
        del self.__value


# Далее используя этот класс создадим два дескриптора в классе Point:

class Point:
    coordX = CoordValue()
    coordY = CoordValue()

    def __init__(self, x = 0 , y = 0):
        self.coordX = x
        self.coordY = y



pt = Point(1, 2)
print(pt.coordX, pt.coordY)
pt.coordX = 100
print(pt.coordX, pt.coordY)
pt2 = Point(4, 6)
print(pt2.coordX, pt2.coordY)
print(pt.coordX, pt.coordY)
