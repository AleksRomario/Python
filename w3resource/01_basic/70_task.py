#!/usr/bin/env python3
"""
Write a Python program to sort files by date.
"""

print("--- my solution ---")



print("--- w3resource solution ---")
import glob
import os

#Модуль glob находит все пути, совпадающие с заданным шаблоном в соответствии с правилами
files = glob.glob("*.py")
# print(type(files))
# результат = list

# сортирует list где key параметр это время последнего изменения файла, в секундах
files.sort(key=os.path.getmtime)
# Возвращает строку, собранную из элементов указанного объекта, поддерживающего итерирование.
print("\n".join(files))
# метод строки с разделителем "\n" для list=files 
