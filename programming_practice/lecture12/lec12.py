#!/usr/bin/env python3

# Пример самодокументирования (писание внятных названий)
def hypotenuse_v1(leg1, leg2):
	return (leg1**2 + leg2**2)**0.5

 
# Применение документации в коде
def hypotenuse_v2(leg1, leg2):
	# Square root from sum of squares of triangle legs.
	# Pifagor. Geometry of Euclid.	
	return (leg1**2 + leg2**2)**0.5 

# Применение докумет строки и аннотации
def hypotenuse_v3(leg1: float, leg2:float) -> float:
	"""
	Calculates lenght of hypotenuse of right triangle.
	:param leg1: Lenght of the first triangle leg
	:param leg2: Lenght of the second triangle leg
	:return:
	"""
	# Square root from sum of squares of triangle legs.
	# Pifagor. Geometry of Euclid.	
	return (leg1**2 + leg2**2)**0.5 


# проверяемое утверждение assert
def hypotenuse_v4(leg1: float, leg2:float) -> float:
	"""
	Calculates lenght of hypotenuse of right triangle.
	:param leg1: Lenght of the first triangle leg
	:param leg2: Lenght of the second triangle leg
	:return:
	"""
	# Square root from sum of squares of triangle legs.
	# Pifagor. Geometry of Euclid.	
	lenght = (leg1**2 + leg2**2)**0.5
	assert lenght**2 == leg1**2 + leg2**2, "Doesn't work!"  
	return lenght 


def main():
	x, y = [float(a) for a in input('ведите гипотенузу 1 и 2 через пробел: ').split()]

	print('Hypotenuse is', hypotenuse_v3(x, y))


if __name__ == "__main__":
	main()

