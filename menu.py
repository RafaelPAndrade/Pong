#coding: utf-8

from printing import words
import pygame
from constants import CFUNDO, FPS, SCREEN_WIDTH, SCREEN_HEIGHT, CLETRA




def menu(display, relógio):

	pong1 = 2
	pong2 = 3
	feito = False

	while not feito:
		display.fill(CFUNDO)

		words(SCREEN_WIDTH/2, SCREEN_HEIGHT*1/14, CLETRA, 70, "PONG", display)


		words(SCREEN_WIDTH/4, SCREEN_HEIGHT*1/7+15, CLETRA, 60, "Options:", display)


		words(SCREEN_WIDTH/4, SCREEN_HEIGHT*1/7+15+30, CLETRA, 30, "(Use numbers to toggle)", display)


		words(SCREEN_WIDTH/8, SCREEN_HEIGHT*2/5, CLETRA, 50, "[1]N Players:", display)

		#secret ingredient over here...
		pongdef1=pong1%2

		if pongdef1 == 0:

			words(SCREEN_WIDTH*3/8, SCREEN_HEIGHT*2/5, CLETRA, 50, "Single-player", display)

		else:  #pongdef1 == 1

			words(SCREEN_WIDTH*3/8, SCREEN_HEIGHT*2/5, CLETRA, 50, "2-player", display)


		words(SCREEN_WIDTH/8, SCREEN_HEIGHT*3/5, CLETRA, 50, "[2]Type of game:", display)


		#secret ingredient over here...
		pongdef2=pong2%3

		if pongdef2 == 2:

			words(SCREEN_WIDTH*3/8, SCREEN_HEIGHT*3/5, CLETRA, 50, "Classic(11)", display)

		elif pongdef2 == 1:

			words(SCREEN_WIDTH*3/8, SCREEN_HEIGHT*3/5, CLETRA, 50, "First to reach 5", display)

		else:  #pongdef2 == 0

			words(SCREEN_WIDTH*3/8, SCREEN_HEIGHT*3/5, CLETRA, 50, "Random", display)






		words(SCREEN_WIDTH*3/4, SCREEN_HEIGHT*1/7+15, CLETRA, 60, "Instructions:", display)


		if pongdef1==0:

			words(SCREEN_WIDTH*3/4, SCREEN_HEIGHT*2/5, CLETRA, 50, "Use [Q]/[A] to move paddle", display)


		else:

			words(SCREEN_WIDTH*3/4, SCREEN_HEIGHT*2/5, CLETRA, 45, "Use [Q]/[A] and [P]/[L] to move paddle", display)




		words(SCREEN_WIDTH*3/4, SCREEN_HEIGHT*3/5, CLETRA, 50, "Press [Y] to pause", display)



		words(SCREEN_WIDTH/2, SCREEN_HEIGHT*12/14, CLETRA, 50, "Press [SPACE BAR] to continue", display)



		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				feito = True
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_1:
					pong1 += 1
				if event.key == pygame.K_2:
					pong2 += 1
				if event.key == pygame.K_3:
					done = True
				if event.key == pygame.K_SPACE:
					feito = True

		pygame.display.flip()
		relógio.tick(FPS)


	return pongdef1, pongdef2
