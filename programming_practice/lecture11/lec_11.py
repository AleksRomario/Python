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

 
class Player:
	'''
	Определяем класс Player который передаем в GameRoundManager
	'''
	pass


class GameField:
	pass


class GameFieldView:
	pass


class GameRoundManager:
	'''
	Менеджер игры, запускающий все процессы 
	'''
	# игроки типа: Player не создаются менеджером, а передаются ему
	def __init__(self, player1:Player, player2:Player):
		# _players с подчеркиванием обозначает свойство не публичное
		# оно явряется внутренним для GameRoundManager 
		self._players = [player1, player2]
		self._current_player = 0  
		self._field = GameField()

	def handle_click(self, event):
		# если клик проишел 
		if 

		player = self._players[self.current_player] 
		# игрок делает клик на поле
			 


class GameWindow:
	'''
	Содержит в себе виджет поля, а так же менеджер игрового раунда
	'''
	def __init__(self):
		# Инициализация pygame
		self._field_widget = GameFieldView()
		# инициализация GameManager, которому передаются игроки (2)
		# Прописываем имена и за кого они играют не запоминая, а 
		# используя локальные имена.
		player1 = Player("Alex", Cell.CROSS)
		player2 = Player("Mike", Cell.ZERO)
		self._game_manager = GameRoundManager(player1, player2) 

	
	# Главный loop игры 
	def main_loop(self):
		finished = False
		# Пока игра прожолжается 
		while not finished:
			# цикл событий
			for event in pygame.get_events(...):
				if event.type == pygame.QUIT:
					finished = True
				# проброс события если клик по полю
				elif event.type == pygame.MOUSEBUTTONDOWN:
					# передаются  координаты x, y в gameField (field_widget) и вытаскиваются i, j 
					x, y = event.x, event.y
					# определяем клик в окне ли или за его границами
					if self._field_widget.check_coords_correct(x, y):
						i, j = self._field_widget.get_coords(x, y)
						self._game_manager.handle_click(x, y)
					 	# LATEST 58:58   
			
 





