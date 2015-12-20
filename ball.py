from block import Block
import constants
import random
import pygame
import paddle

class Ball(Block):
	def __init__(self, x, y, color):
		super().__init__(x,y,15,15,constants.CBALL)
		self.colliders = None
		
		
		if random.random() > 0.5:
			sign = -1
		else:
			sign = 1
		self.dir_x = random.randrange(2,4) * sign
		self.dir_y = random.randrange(-4,4)




	def set_colliders(self, colliders):
			self.colliders = colliders	


	def update(self):

		
		self.rect.y += self.dir_y
		collision_list = pygame.sprite.spritecollide(self, self.colliders, False)
		if len(collision_list) >  0:
			#se nos estamos a mover paracima
			if self.dir_y < 0 :
				if self.rect.top < collision_list[0].rect.bottom:
					self.rect.top = collision_list[0].rect.bottom
					self.dir_y = -self.dir_y
			
				
			elif self.dir_y > 0 :
				if self.rect.bottom > collision_list[0].rect.top:
					self.rect.bottom = collision_list[0].rect.top
					self.dir_y = -self.dir_y
		
		
		self.rect.x += self.dir_x
		collision_list = pygame.sprite.spritecollide(self, self.colliders, False)
		if len(collision_list) >  0:
			#se nos estamos a mover para lado
			if self.dir_x < 0 :
				if self.rect.left < collision_list[0].rect.right:
					self.rect.left = collision_list[0].rect.right
					self.dir_x = -self.dir_x * (random.randrange(90, 175)/100)
					if self.dir_x >= 8:
						self.dir_x = 8
					if self.dir_x <= -8:
						self.dir_x = -8
					self.dir_y = -self.dir_y + (collision_list[0].change_y/3)
						
			elif self.dir_x > 0 :
				if self.rect.right > collision_list[0].rect.left:
					self.rect.right = collision_list[0].rect.left
					self.dir_x = -self.dir_x * (random.randrange(90,175)/100)
					if self.dir_x >= 9:
						self.dir_x = 9
					if self.dir_x <= -9:
						self.dir_x = -9					
					self.dir_y = -self.dir_y + (collision_list[0].change_y/3) 
