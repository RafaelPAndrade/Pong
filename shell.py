#coding: utf-8

import pygame


from lib.printing import words
from lib.constants import SCREEN_WIDTH, SCREEN_HEIGHT
from lib.menu import menu
from lib.jogo import jogo
from lib.postgame import postgame


# Inicializao da biblioteca pygame
pygame.init()

# Criação da janela com a resolução indicada
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# Definição do título da janela
pygame.display.set_caption('Pong')

# inicializar o relógio
clock = pygame.time.Clock()

ação = 0
done = False

while not done:

	if ação == 0:
		pongdef1, pongdef2 = menu(screen, clock)
		ação = 1

	print(pongdef1, pongdef2)


	if ação == 1:
		ganhou, pontos1, pontos2 = jogo(pongdef1, pongdef2, screen, clock)
		print(ganhou)
		ação = postgame(ganhou, pontos1, pontos2, screen, clock)
		print(ação)


	if ação == 2:
		done = True

pygame.quit()
