#!/usr/bin/env python3
"""
Write a Python program to get file creation and modification date/times.
"""

print("--- my solution ---")
import os 
import time
import datetime
file_creation = os.path.getctime("63_task.py")
file_modification = os.path.getmtime("63_task.py")
datenow = datetime.datetime.now() 
datecreate  = datetime.datetime.fromtimestamp(file_creation)
datemodificate = datetime.datetime.fromtimestamp(file_modification)
print("Время сейчас: ", datenow)
print("Создание файла: ", datecreate)
print("Изменение файла: ", datemodificate)

print("--- w3resource solution ---")

import os.path, time
print("Last modified: %s" % time.ctime(os.path.getmtime("63_task.py")))
print("Created: %s" % time.ctime(os.path.getctime("63_task.py")))
print("Current time from me: %s" % time.ctime())

