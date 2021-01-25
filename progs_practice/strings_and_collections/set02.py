#!/usr/bin/env python3

# Операции над множествами
# Определение длинны set: 
s = {1, 2, 3, 4, 5}
print(len(s))

# Для проверки наличия экземпляра в множестве используется конструкция: 
answer = 1 in s
print(answer)
answer = 6 not in s
print(answer)

# Пересечение множеств:
# Результатом сравнение создается новое множество
s1 = {1, 2, 3, 4, 5}
s2 = {3, 4, 5, 6, 7}
# можно определять пересечение, значение которые входят в состав обоих set
common = s1 & s2
# или более короткая запись где одно из множеств будет содержать только пересечение 
s1 &= s2
print(common, type(common))
print(s1, type(s1))

# В случае если пересечение отсутствует, будет созданно пустое множество
# Используемый оператор можно изменить на эквивалентный метод intersection
setA = {1, 2, 3, 4, 5}
setB = {3, 4, 5, 6, 7}
setC = setA.intersection(setB)
print(setC, type(setC))
# сами множества остаются без изменений 
# в случае как с короткой записью можно использовать 
setA.intersection_update(setB)
print(setA, type(setA))

# Объединение множества 
setA = {"a", "b", "c"}
setB = {"c", "d", "e"}
setC = setA | setB
print(setC, type(setC))
# Альтернативное написание с помощью union: 
setC = setA.union(setB)
print(setC, type(setC))

# Вычитание множеств
# Исключение значение которые входят в оба множества
setC = setA - setB
print(setC, type(setC))
setC = setB - setA
print(setC, type(setC))

# можно использовать короткие записи 
# setA -= setB  # setA = setA - setB
# setB -= setA  # setB = setB - setA

# Симетричность множеств
# В результате получим только уникальные значения для обоих множеств
setC = setA ^ setB
print(setC, type(setC))

# Сравнение множеств
result = setA == setB # проверка равенства
print(result, type(result))
result = setA != setB # проверка неравенства
print(result, type(result))

# На больше, меньше
# Проверка вхождения одного множества в другое
# Входит если элементы одного множества принадлежат другому множеству
setA = {1, 2, 3, 4, 5, 6, 7}
setB = {3, 4, 5, 6}
result = setA < setB # False, так как setA не входит в setB
print(result)
result = setA > setB # True, так как setB  входит в setA
print(result)
# Для равных множеств операция вхождения вернет False 

setA = {1, 2, 3}
setB = {1, 2, 3}
result = setA > setB
print(result)
# Но оператор >= или <= вернет True 
result = setA >= setB
print(result)


# Задание для самоподготовки 
# напишите программу, которая из введенного с клавиатуры текста определяет число уникальных слов. Для простоты можно полагать, что слова разделяются пробелом или символом переноса строки ‘\n’.
