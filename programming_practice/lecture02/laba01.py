#!/usr/bin/env python3

import turtle 

# Задача нарисовать квадрат. 
print("Press number to execute programm:")
print("Existing programs to chose: Square: 1, Circle: 2,  ")

def square():
	turtle.shape('turtle')
	turtle.forward(50)
	turtle.left(90)
	turtle.forward(50)
	turtle.left(90)
	turtle.forward(50)
	turtle.left(90)
	turtle.forward(50)
	turtle.left(90)
def circle():
	turtle.shape('turtle')

n = int(input("Your test nember: "))

if n == 1: 
	square()
	input("Promt RETURN for EXIT")
elif n == 2:
	circle()
	input("Promt RETURN for EXIT")
else:
	print("There is no such test")




