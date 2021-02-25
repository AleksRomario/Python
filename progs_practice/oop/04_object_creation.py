#!/usr/bin/env python3
print("--- Создание объектов-своиств  ---")

# Рассмотрение объектов свойств
# Предположим хотим в класе обратится к свойству coordX для записи и чтения
# данных с дополнительной проверкой корректности записи/чтения
# pt.coordX = 100 - запись значения 
# x = pt.coordX - чтение значения


class Point():
    
    def __init__(self, x = 0, y = 0):
        print("Вызов __init__")
        self.__x = x
        self.__y = y
    
    def __getCoordX(self):
        print("Вызов __getCoordX")
        return self.__x

    def __setCoordX(self, x):
        print("Вызов __setCoordX")
        if Point.__checkValue(x):
            self.__x = x
        else:
            print('ValueError("Неверный формат")')

    def __checkValue(x):
        print("Вызов __checkValue")
        if isinstance(x, int) or isinstance(x, float):
            return True
        else:
            return False
    
    def __delCoordX(self):
        print("Вызов __delCoord")
        del self.__x
    # у свойства может быть третий метод вызываемый при удалении 
    # четвертым методом можно записать описание свойства 
    coordX = property(__getCoordX, __setCoordX, __delCoordX , "Работа с X")
    
    # таким же образом можно реализовать доступ к свойствам Y и Z
    # но что бы не повторятся реализуется с помощью дискриптора

# Создание экземпляра класса 
print("-- Создание экземпляра класса Point --")
pt = Point()
print("\n")
print("--запос координаты --")
print( pt.coordX )
print("\n")
print("-- Присвоение новой величины --")
pt.coordX = 100
print("\n")
print("--запос координаты --")
print( pt.coordX )
print("\n")
print("-- Присвоение новой НЕ ВЕНРНОЙ величины --")
pt.coordX = "a"
print("\n")
print("-- Удаление параметра (значения) --")
del pt.coordX

# пример с применением декоратора
# пропишем так же для изменения X что бы сделать так же для Y и Z  
# и не повторяться , необходимо применить дескрипторы.

class Point3d():
    
    def __init__(self, x = 0, y = 0, z = 0):
        print("Вызов __init__")
        self.__x = x
        self.__y = y
        self.__z = z
    
    # перед геттером указывается декоратор @property и название метода 
    # должно совпадать с нахванием свойства:

    # добавляется @property и имя метода меняется на coordX
    @property
    def coordX(self):
        print("Вызов __getCoordX (getter)")
        return self.__x
    
    # добавляется @coordX.setter и имя метода меняется на coordX
    @coordX.setter
    def coordX(self, x):
        print("Вызов __setCoordX (setter)")
        if Point3d.__checkValue(x):
            self.__x = x
        else:
            print('ValueError("Неверный формат")')
    
    def __checkValue(x):
        print("Вызов __checkValue")
        if isinstance(x, int) or isinstance(x, float):
            return True
        else:
            return False
    
    # добавляется @coordX.deleter и имя метрда меняется на coordX
    @coordX.deleter
    def coordX(self):
        print("Вызов __delCoord (deleter)")
        del self.__x

print("-- Создание экземпляра класса Point3d --")
pt = Point3d()
print("\n")
print("--запос координаты --")
print( pt.coordX )
print("\n")
print("-- Присвоение новой величины --")
pt.coordX = 100
print("\n")
print("--запос координаты --")
print( pt.coordX )
print("\n")
print("-- Присвоение новой НЕ ВЕНРНОЙ величины --")
pt.coordX = "a"
print("\n")
print("-- Удаление параметра (значения) --")
del pt.coordX

