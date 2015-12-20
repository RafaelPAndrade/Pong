#coding: latin-1

import pygame
import constants
from block import Block

class Paddle(Block):
	""" Esta classe representa uma raquete do jogo """
	def __init__(self, x, y, height, color):
		super().__init__(x,y,15,height,color)
		self.change_y = 0
		self.walls = None

	def move_up(self):
		self.change_y = -constants.VEL

	def move_down(self):
		self.change_y = constants.VEL

	def dont_move(self):
		self.change_y = constants.NULL
	
	
	def set_walls(self, walls):
		self.walls = walls
	
	
	def update(self):
		# atualizar a posição da raquete
		self.rect.y += self.change_y
		collision_list = pygame.sprite.spritecollide(self, self.walls, False)
		# se houver pelo menos um objeto na lista de colisoes... inversao de marcha
		if len(collision_list) >  0:
			#se nos estamos a mover paracima
			if self.change_y < 0:
				if self.rect.top < collision_list[0].rect.bottom:
					self.rect.top = collision_list[0].rect.bottom
		
			elif self.change_y > 0 :
				if self.rect.bottom > collision_list[0].rect.top:
					self.rect.bottom = collision_list[0].rect.top
