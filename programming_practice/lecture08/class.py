#!/usr/bin/env python3

class Dragon:

	def __init__(self, name, health):
		self.name = name
		self.health = health


	def is_alive(self):
		return self.health > 0


	def get_damage(self, damage):
		print('You dameged me for', damage, 'points')
		self.health -= damage
		if self.health < 0:
			self.health = 0 


	def talk(self):
		print(self.name,' health', self.health, '. Hit me!')


def main():
	dragon = Dragon(
	(input("Input the enemy name!")),
	(int(input("Input enemy healt")))
	)
	finished = False 
	while not finished:	
		dragon.talk()
		damage = int(input('How muck damage you need to deal? : '))
		dragon.get_damage(damage)
		if not dragon.is_alive():
			finished = True
	print('Dragon slayed. Game over!!!')

main()

