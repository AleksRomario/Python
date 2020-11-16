#!/usr/bin/env python3

# создаение кода с точки зрения проектирования. 
def main():
	x, y = 100, 100
	width, height = 100, 100

	draw_house(x, y, width, height)


def draw_house(x, y, width, height):
	'''
	Функция рисует домик ширины width и height от пророной точки (x, y),
	которая находится в середине нижней точки фундамента
	:param x: координа x середины домика 
	:param y: коотдинаты y низа фундамента 
	:param width: полная ширина домика (фундамент или вылет крыши включены)
	:param height: полная высота домика
	:return: None
	'''
	print('переданные данные в функцию', x, y , width , height)
	foundation_height = 0.05 * height 
	walls_width = 0.9 * width 
	walls_height = 0.5 * height 
	roof_height = height - foundation_height - walls_height

	draw_house_foundation (x, y , width, foundation_height)
	draw_house_walls(x, y, walls_width, walls_height)
	draw_house_roof(x, y , width, roof_height)


def draw_house_foundation(x, y, width , height):
	'''
	Нарисовать основание дома ширины width и высоты height от опорной точки (x, y),
	которая находится в середине нижней точки фундамента.
	:param x: координа x середины домика 
	:param y: коотдинаты y низа фундамента 
	:param width: полная ширина домика
	:param height: полная высота домика
	:return: Non
	'''
	print('Типо рисую основание с данными:', x, y , width, height)
	pass


def draw_house_walls(x, y, width , height):
	'''
	Нарисовать стены  дома ширины width и высоты height от опорной точки (x, y),
	которая находится в середине нижней точки фундамента.
	:param x: координа x середины домика 
	:param y: коотдинаты y низа фундамента 
	:param width: полная ширина домика
	:param height: полная высота домика
	:return: Non
	'''
	print('Типо рисую стены с данными:', x, y , width, height)
	pass


def draw_house_roof(x, y, width , height):
	'''
	Нарисовать основание дома ширины width и высоты height от опорной точки (x, y),
	которая находится в середине нижней точки фундамента.
	:param x: координа x середины домика 
	:param y: коотдинаты y низа фундамента 
	:param width: полная ширина домика
	:param height: полная высота домика
	:return: Non
	'''
	print('Типо рисую крышу с данными:', x, y , width, height)
	pass



if __name__ == "__main__":
	main()


