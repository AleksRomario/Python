#!/usr/bin/env python3

# иерархия классов

class Base:
	def __init__(self, x):
		self.x = x
	
	def show(self):
		print('Base class', self.x)
 
class Derivative(Base):
	def __init__(self):
		# так как не передается параметр инициализации x, необходимо
		# его явно передать в Base класс
		Base.__init__(self, 20) 
		# Или альтернативно super().__init__(20) - явный вызов конструктора. 
		# что будет означать обращение к родительскому классу. 
		# Преимущественно обращаться через super, а не по имени класса
		# так как не надо будет указывать имя класса. 
		# В случае если родительских классов несколько, то обращаться 
		# придется явно упоминая имя класса
		# super() - фунуция возвращающая надкласс 
		self.name = 'Alex'


a = Base(10)
b = Derivative()
a.show()
b.show()
 
