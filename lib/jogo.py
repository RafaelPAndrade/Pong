#coding: utf-8
import pygame
import random

from .printing import words
from .paddle import Paddle
from .wall import Wall
from .ball import Ball
from .block import Block
from .constants import SCREEN_WIDTH, SCREEN_HEIGHT, CWALLS, CPLAYER1, CPLAYER2, CBALL, CFUNDO, Height1, Height2, RED, FPS



def jogo(def1, def2, display, relógio):

	if def2 == 0:
		maxscore = random.randint(3,8)
	elif def2 == 1:
		maxscore = 5
	elif def2 == 2:
		maxscore = 11

	print("maxscore = ", maxscore)


	""" listas para gerir os vários objetos do jogo """
	# criação do grupo dos objetos que necessitam ser redesenhados (todos)
	drawables_list = pygame.sprite.Group()

	#criação do grupo dos objetos que colidem com a bola
	colliders_list = pygame.sprite.Group()

	#criação do grupo dos objetos animados
	animated_list = pygame.sprite.Group()

	# criar as paredes
	top_wall = Wall(0, 0, SCREEN_WIDTH, CWALLS)
	colliders_list.add(top_wall)
	drawables_list.add(top_wall)

	bottom_wall = Wall(0, SCREEN_HEIGHT-15, SCREEN_WIDTH, CWALLS)
	colliders_list.add(bottom_wall)
	drawables_list.add(bottom_wall)

	#todas as paredes, necessario para a bola?
	walls_list = pygame.sprite.Group()
	walls_list.add(top_wall)
	walls_list.add(bottom_wall)


	# criar a rede e adicionar os objetos à lista de objetos que necessitam ser $
	for i in range(0, SCREEN_HEIGHT, 30):
			net = Block(SCREEN_WIDTH//2-12, i-10, 12, 15, CWALLS)
			drawables_list.add(net)


	#---------coisas:tipo de jogo, pontuações, o resultado para ganhar, cores---$
	score1 = 0							#score player 1
	score2 = 0							#score player 2
	winplayer = 0							#que jogador ganhou
	scoreTot = str(score1) + "      " + str(score2)			#string que comporta o score, acho que não devia estar aqui
	match = False							#se há matchpoint
	pause = False							#se estamos em pausa a meio do jogo
	player = False
	ball = None
	#------------------------------------------------------------------


	while winplayer == 0 :

	#--------paddle height--------------
		if match == False:
			Comprimento1 = Height1
			Comprimento2 = Height2
		elif match == True:
			if score1 >= score2:
				Comprimento1 = Height1*2/3
			if score2 >= score1:
				Comprimento2 = Height2*2/3



		if player == False:
			if match == False:

				player_one = Paddle(30, SCREEN_HEIGHT//2-30, Comprimento1, CPLAYER1)
				player_two = Paddle(SCREEN_WIDTH-30-15, SCREEN_HEIGHT//2-30, Comprimento2, CPLAYER2)


				player_one.set_walls(walls_list)
				player_two.set_walls(walls_list)
				colliders_list.add(player_one)
				colliders_list.add(player_two)
				drawables_list.add(player_one)
				drawables_list.add(player_two)
				animated_list.add(player_one)
				animated_list.add(player_two)
				player = True

			if match == True:

				player_one.kill()
				player_two.kill()

				player_one = Paddle(30, SCREEN_HEIGHT//2-30, Comprimento1, CPLAYER1)
				player_two = Paddle(SCREEN_WIDTH-30-15, SCREEN_HEIGHT//2-30, Comprimento2, CPLAYER2)


				player_one.set_walls(walls_list)
				player_two.set_walls(walls_list)
				colliders_list.add(player_one)
				colliders_list.add(player_two)
				drawables_list.add(player_one)
				drawables_list.add(player_two)
				animated_list.add(player_one)
				animated_list.add(player_two)
				player = True


		# Verificar se é necessário criar uma nova bola e coloca os players $
		if ball == None:
			ball = Ball(SCREEN_WIDTH//2-7, SCREEN_HEIGHT//2-7, CBALL)
			ball.set_colliders(colliders_list)
			# adicionar a bola à lista de objetos a atualizar
			animated_list.add(ball)
			drawables_list.add(ball)

			if score1 == 0 and score2 == 0:
				ball.dir_x = ball.dir_x
				ball.dir_y = 0
				player_one.rect.y = SCREEN_HEIGHT//2-30
				player_two.rect.y = SCREEN_HEIGHT//2-30



		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True
				winplayer = -1
			if event.type == pygame.KEYDOWN:
				if pause == False:
					if event.key == pygame.K_q or event.key == pygame.K_UP and def1 == 0:
						player_one.move_up()
					elif event.key == pygame.K_a or event.key == pygame.K_DOWN and def1 == 0:
						player_one.move_down()
					elif event.key == pygame.K_p and def1 == 1 or event.key == pygame.K_UP and def1 == 1:
						player_two.move_up()
					elif event.key == pygame.K_l and def1 == 1 or event.key == pygame.K_DOWN and def1 == 1:
						player_two.move_down()

			if event.type == pygame.KEYUP:
				if event.key == pygame.K_y:
					if pause == False:
						pause = True
					elif pause == True:
						pause = False
				if event.key == pygame.K_q:
					player_one.dont_move()
				elif event.key == pygame.K_a:
					player_one.dont_move()
				elif event.key == pygame.K_p:
					player_two.dont_move()
				elif event.key == pygame.K_l:
					player_two.dont_move()
				if def1 == 0:
					if event.key == pygame.K_UP:
						player_one.dont_move()
					elif event.key == pygame.K_DOWN:
						player_one.dont_move()
				elif def1 == 1:
					if event.key == pygame.K_UP:
						player_two.dont_move()
					elif event.key == pygame.K_DOWN:
						player_two.dont_move()



		if player == True and def1 == 0:
			if player_two.rect.y + Height2/2 <= ball.rect.y + 7:
				player_two.move_down()
			elif player_two.rect.y + Height2/2 >= ball.rect.y + 7:
				player_two.move_up()



		"""--------------------------------------------- A lógica do jogo ----------------------------------------"""

		# Testar se a bola sai pela esquerda (ponto para o jogador 2)
		if ball.rect.x < - 10 or ball.rect.x > SCREEN_WIDTH + 10 :
			#Ponto para o jogador 2
			if ball.rect.x < -10 :
				score2 += 1
				ball.kill()
				ball = None

			#Ponto para o jogador 1
			elif ball.rect.x > SCREEN_WIDTH + 10 :
				score1 += 1
				ball.kill()
				ball = None

			scoreTot = str(score1) + "     " + str(score2)
			#print(scoreTot)



			#-------------------MatchPoint---------------------------

			#estilo 1 ou 0
			if def2 == 1 or def2 ==0:
				if score1+1 == maxscore:
					match = True
					player = False

				elif score2+1 == maxscore:
					match = True
					player = False

			#estilo 2
			if def2 == 2:
				if score1+1 == 6 and score2 == 0:
					match = True
					player = False
				elif score1+1 == 7 and score2 == 1:
					match = True
					player = False
				elif score2+1 == 6 and score1 == 0:
					match = True
					player = False
				elif score2+1 == 7 and score1 == 1:
					match = True
					player = False
				elif score1+1 >= maxscore and score1 - score2 >= 2:
					match = True
					player = False
				elif score2+1 >= maxscore and score2 - score1 >= 2:
					match = True
					player = False
				else:
					match = False
				#	player = False
				#	player_one.kill()
				#	player_two.kill()

			#-----------------------Win---------------------------
			#
			#nos jogos 1 e 2, só interessa quem chega ao resultado primeiro

			if score1 >= maxscore and def2 != 2:
				winplayer = 1
			elif score2 >= maxscore and def2 != 2:
				winplayer = 2

			#Existem capotes...
			if def2 == 2:
				if score1 == 6 and score2 == 0:
					winplayer = 1
				elif score1 == 7 and score2 == 1:
					winplayer = 1
				elif score2 == 6 and score1 == 0:
					winplayer = 2
				elif score2 == 7 and score1 == 1:
					winplayer = 2
				elif score1 >= maxscore and score1 - score2 >= 2:
					winplayer = 1
				elif score2 >= maxscore and score2 - score1 >= 2:
					winplayer = 2








		display.fill(CFUNDO)
		drawables_list.draw(display)

		if pause == False:
			animated_list.update()

		#--------------------------------------------Pontuação--------------------------------
		if match == False: #se não for matchpoint

			words(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, CWALLS, 150, scoreTot, display)


		elif match == True: #se for matchpoint

			words(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, RED, 150, scoreTot, display)


		#-------------------------Pausa--------------------------

		if pause == True:

			words(SCREEN_WIDTH/2, SCREEN_HEIGHT*2/3, CWALLS, 115, " Get        Ready", display)

		# atualizar o ecrã com o conteúdo desenhado
		pygame.display.flip()

		relógio.tick(FPS)


	return winplayer, score1, score2


