#coding: utf-8


import pygame
from printing import words
from constants import CWALLS, SCREEN_WIDTH, SCREEN_HEIGHT, CFUNDO, FPS




def postgame(ganha, score1, score2, display, relógio):

	if ganha == 1:
		winstring = "Player 1 wins!"
	elif ganha == 2:
		winstring = "Player 2 wins!"

	escolha = False

	while not escolha:

	#-----------------1st- Player x wins
		display.fill(CFUNDO)

		words(SCREEN_WIDTH/2, SCREEN_HEIGHT*4/15, CWALLS, 150, winstring, display)

	#---------------Resultado final
		score1 = score1
		score2 = score2
		score_Tot = str(score1) + "-" + str(score2)

		words(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, CWALLS, 65, score_Tot, display)


	#---------------Recomeçar?


		words(SCREEN_WIDTH/2, SCREEN_HEIGHT/2+75, CWALLS, 50, "Press [G] to restart, [Y] for Menu and [B] to exit", display)





		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_g:
					action = 1
				if event.key == pygame.K_y:
					action = 0
				if event.key == pygame.K_b:
					action = 2
				escolha = True
			if event.type == pygame.QUIT:
				escolha = True

		pygame.display.flip()
		relógio.tick(FPS)


	return action

