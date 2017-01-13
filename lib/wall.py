import pygame

from .block import Block

class Wall(Block):
	""" Classe para representar as paredes do jogo, onde a bola vai tabelar """
	def __init__(self, x, y, width, color):
		super().__init__(x, y, width, 15, color)
		self.change_y=0
