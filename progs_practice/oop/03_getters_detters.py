#!/usr/bin/env python3
print("--- Режимы доступа, геттеры и сеттеры ---")

# Ограничение доступа к данным и методам извне - инкапсуляция
# Обращение к приватным свойствам черех геттеры и сеттеры

class Point():
    
    def __init__(self, x = 0, y = 0):
        self.x = x 
        self.y = y

pt = Point(1, 2)
# Выводим параметры
print(pt.x , pt.y)
# Доступ к параметрам напрымую 
pt.x = 100
pt.y = "Hello"
print(pt.x , pt.y)
print("\n")

# дабы избежать прямого доступа используются геттеры и сеттеры 

# 1. <имя атрибута> (без одного или двух подчеркиваний вначале) – публичное 
# свойство (public);

# 2. _<имя атрибута> (с одним подчеркиванием) – режим доступа protected 
# (можно обращаться только внутри класса и во всех его дочерних классах)

# 3. __<имя атрибута> (с двумя подчеркиваниями) – режим доступа private 
# (можно обращаться только внутри класса).

class Point3d():
    
    WIDTH = 9
    HEIGHT = 11
    
    def __init__(self, x = 0, y = 0, z =0):
        self.__x = x 
        self.__y = y
        self.__z = z

    def setPoint3d(self, x, y, z):
        if Point3d.__checkValue(x) and Point3d.__checkValue(y) and  Point3d.__checkValue(z):
            self.__x = x
            self.__y = y
            self.__z = z
        else:
            print("Параметры должны быть цифрами")

    def getPoint3d(self):
        return self.__x, self.__y, self.__z

    def __checkValue(val):
        if isinstance(val, int) or  isinstance(val, float):
            return True
        return False

    def __getattribute__(self, item):
        if item == "_Point3d__x":
            return "Private attribute"
        else:
            return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        if key == "WIDTH":
            print("Can't change Value")
        else:
            self.__dict__[key] = value
            print(self.HEIGHT)


print("Инициализируем переменные:")
pt3d = Point3d(1, 2, 3)
print(pt3d.__dict__)
print("\n")
print("Изменяем переменные:")
pt3d.setPoint3d(11, 12, 13)
print(pt3d.__dict__)
print("\n")
print("Достаем переменные:")
print(pt3d.getPoint3d())
print("\n")
print("Изменяем параметы: Неправильный формат")
pt3d.setPoint3d(1, 1, "a")
print("\n")
print("Обращение на прямую к свойствам извне")
# все же возможно обратится к параметрам которые protected
# обращение происходит по шаблону:
# _Имя класса__имя переменной
# _Имя класса__имя метода
pt3d._Point3d__x = 99
print(pt3d.__dict__)
print(pt3d._Point3d__x)
print(pt3d._Point3d__y)
print("\n")
print("Изменение параметра в классе")
pt3d.WIDTH = 16
pt3d.HEIGHT = 16

# При необходимости мы можем осуществлять дополнительный контроль 
# изменения атрибутов, путем перегрузки следующих методов:

# __setattr(self, key, value)__ – автоматически вызывается при изменении свойства key класса;
# __getattribute__(self, item) – автоматически вызывается при получении свойства класса с именем item;
# __getattr__(self, item) – автоматически вызывается при получении несуществующего свойства item класса;
# __delattr__(self, item) – автоматически вызывается при удалении свойства item (не важно: существует оно или нет).

