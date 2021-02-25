#!/usr/bin/env python3
"""
Write a Python program to convert seconds to day, hour, minutes and seconds. 
"""

print("--- my solution ---")

seconds = int(input("Enter required seconds to convert: "))

def convertSeconds(sec = 6000):
    s_convert = sec
    days = s_convert // (3600 * 24 )
    s_convert = s_convert % (3600 * 24)   
    hours = s_convert // 3600
    s_convert = s_convert %  3600  
    minutes = s_convert // 60
    seconds = s_convert % 60 
    print("convertation result: ")
    print(days)
    print(hours)
    print(minutes)
    print(seconds)

convertSeconds(seconds)
print("--- w3resource solution ---")

time = float(input("Input time in seconds: "))
day = time // (24 * 3600)
time = time % (24 * 3600)
hour = time // 3600
time %= 3600
minutes = time // 60
time %= 60
seconds = time
print("d:h:m:s-> %d:%d:%d:%d" % (day, hour, minutes, seconds))
