#!/usr/bin/env python3

#Cross and zeros game 
from enum import Enum

class Cell(Enum):
	VOID = 0
	CROSS = 1
	ZERO = 2


class Player:
	'''
	Класс игрока, содержащий тип значков и имя
	'''
	pass


class GameRoundManager:
	'''
	Менеджер игры, запускающий все процессы 
	'''
	# игроки типа: Player не создаются менеджером, а передаются ему
	def __init__(self, player1:Player, player2:Player): 
		self.players = [player1, player2]
	
	# Главный loop игры 
	def main_loop(self):
		# Пока игра прожолжается 
		while not game_over:
			player = next_player() 

 
class Player:
	'''
	Определяем класс Player который передаем в GameRoundManager
	'''
	pass


class GameField:
	pass


class GameFieldView:
	pass


class GameWindow:
	pass


