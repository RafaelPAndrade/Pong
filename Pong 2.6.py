
import pygame
import random
from block import Block
from printing import words
from paddle import Paddle
from wall import Wall
from ball import Ball
from constants import BLACK, RED, CPLAYER1, CPLAYER2, CWALLS, CBALL, CFUNDO, SCREEN_WIDTH, SCREEN_HEIGHT, FPS, Height1, Height2

# Inicializao da biblioteca pygame
pygame.init()

# Criação da janela com a resolução indicada
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# Definição do título da janela
pygame.display.set_caption('Pong')



# inicializar o relógio
clock = pygame.time.Clock()


# variável usada para assinalar que o jogo terminou
done = False


# criar as paredes
top_wall = Wall(0, 0, SCREEN_WIDTH, CWALLS)
bottom_wall = Wall(0, SCREEN_HEIGHT-15, SCREEN_WIDTH, CWALLS)

#todo -paredes
walls_list = pygame.sprite.Group()

walls_list.add(top_wall)
walls_list.add(bottom_wall)



ball = None
player = False

""" listas para gerir os vários objetos do jogo """
# criação do grupo dos objetos que necessitam ser redesenhados (todos)
drawables_list = pygame.sprite.Group()

#criação do grupo dos objetos que colidem com a bola
colliders_list = pygame.sprite.Group()

#criação do grupo dos objetos animados
animated_list = pygame.sprite.Group()



# adicionar as paredes superior e inferior aos objetos que colidem com a bola
colliders_list.add(top_wall)
colliders_list.add(bottom_wall)


# adicionar os objetos que necessitam ser desenhados
drawables_list.add(top_wall)
drawables_list.add(bottom_wall)

# criar a rede e adicionar os objetos à lista de objetos que necessitam ser redesenhados
for i in range(0, SCREEN_HEIGHT, 30):
	net = Block(SCREEN_WIDTH//2-12, i-10, 12, 15, CWALLS)
	drawables_list.add(net)


#---------coisas:tipo de jogo, pontuações, o resultado para ganhar, cores--------------------
#style = 0 					#tipo de jogo, extinto-->pongdef2
score1 = 0 					#score player 1
score2 = 0					#score player 2
winplayer = 0					#que jogador ganhou
scoreTot = str(score1) + "   " + str(score2) 	#string que comporta o score, não funciona a partir daqui
maxscore = 1					#pontos máximos (até aos maxscore pontos)
match =	False					#se há matchpoint
single = False					#se é singleplayer (pongdef1), não pode ser extinto por design por agora...
pause = False					#se estamos em pausa a meio de um jogo
pong1 = 2					#valores iniciais do pongdef1 (0)
pong2 = 3					#e pongdef2(0)
menu = True					#Comeback! se temos menu (antes Intro)
#------------------------------ciclo principal---------------------------------------------
while not done:

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

		elif match == True:
			player_one.kill()
			player_two.kill()

			player_one = Paddle(30, SCREEN_HEIGHT//2-30, Comprimento1, CPLAYER1)
			player_two = Paddle(SCREEN_WIDTH-30-15, SCREEN_HEIGHT//2-30, Comprimento2, CPLAYER2)

			player_one = Paddle(30, SCREEN_HEIGHT//2-30, Height1, CPLAYER1)
			player_one.set_walls(walls_list)
			player_two.set_walls(walls_list)
			colliders_list.add(player_one)
			colliders_list.add(player_two)
			drawables_list.add(player_one)
			drawables_list.add(player_two)
			animated_list.add(player_one)
			animated_list.add(player_two)
			player = True



	# Verificar se é necessário criar uma nova bola e coloca os players nos sítios
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
		if event.type == pygame.KEYDOWN:
			if pause == False:
				if event.key == pygame.K_q or event.key == pygame.K_UP and single == True:
					player_one.move_up()
				elif event.key == pygame.K_a or event.key == pygame.K_DOWN and single == True:
					player_one.move_down()
				elif event.key == pygame.K_p and single == False or event.key == pygame.K_UP and single == False:
					player_two.move_up()
				elif event.key == pygame.K_l and single == False or event.key == pygame.K_DOWN and single == False:
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
			if single == True:
				if event.key == pygame.K_UP:
					player_one.dont_move()
				elif event.key == pygame.K_DOWN:
					player_one.dont_move()
			elif single == False:
				if event.key == pygame.K_UP:
					player_two.dont_move()
				elif event.key == pygame.K_DOWN:
					player_two.dont_move()




	if player == True and single == True:
		if player_two.rect.y + Height2/2 <= ball.rect.y + 7:
			player_two.move_down()
		elif player_two.rect.y + Height2/2 >= ball.rect.y + 7:
			player_two.move_up()
		#player_two.change_y = player_two.change_y*2/3

	#if player == True and menu == True:  #demo
	#	if player_two.rect.y + Height2//2 <= ball.rect.y + 7:
	#		player_two.move_down()
	#	elif player_two.rect.y + Height2//2 >= ball.rect.y + 7:
	#		player_two.move_up()
	#	if player_one.rect.y + Height2//2 <= ball.rect.y + 7:
	#		player_one.move_down()
	#	elif player_one.rect.y + Height2//2 >= ball.rect.y + 7:
	#		player_one.move_up()






	"""--------------------------------------------- A lógica do jogo ----------------------------------------"""

	# Testar se a bola sai pela esquerda (ponto para o jogador 2)
		#Ponto para o jogador 2
	if ball.rect.x < - 10 or ball.rect.x > SCREEN_WIDTH + 10 :
		if ball.rect.x < -10 :
			score2 += 1
			ball.kill()
			ball = None


		#Ponto para o jogador 1
		elif ball.rect.x > SCREEN_WIDTH + 10 :
			score1 += 1
			ball.kill()
			ball = None

		scoreTot = str(score1) + "   " + str(score2)
		print(scoreTot)

#-------------------MatchPoint---------------------------

		#estilo 1 ou 0
		if pongdef2 == 1 or pongdef2 ==0:
			if score1+1 == maxscore:
				match = True
				player = False

			elif score2+1 == maxscore:
				match = True
				player = False

		#estilo 2
		if pongdef2 == 2:
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
				player = False
				player_one.kill()
				player_two.kill()

		#-----------------------Win---------------------------
		#
		#nos jogos 1 e 2, só interessa quem chega ao resultado primeiro

		if score1 >= maxscore and pongdef2 != 2:
			winplayer = 1
		elif score2 >= maxscore and pongdef2 != 2:
			winplayer = 2

		#Existem capotes...
		if pongdef2 == 2:
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





	# limpar o fundo do ecrã
	screen.fill(CFUNDO)
	# desenhar tudo o que é visível 	# Display some text



	#-----------------Intro---------------------


	if menu == True:

		words(SCREEN_WIDTH/2, SCREEN_HEIGHT*1/14, BLACK, 70, "PONG", screen)


		words(SCREEN_WIDTH/4, SCREEN_HEIGHT*1/7+15, BLACK, 60, "Options:", screen)


		words(SCREEN_WIDTH/4, SCREEN_HEIGHT*1/7+15+30, BLACK, 30, "(Use numbers to toggle)", screen)


		words(SCREEN_WIDTH/8, SCREEN_HEIGHT*2/5, BLACK, 50, "[1]N Players:", screen)

		#secret ingredient over here...
		pongdef1=pong1%2

		if pongdef1 == 0:

			words(SCREEN_WIDTH*3/8, SCREEN_HEIGHT*2/5, BLACK, 50, "Single-player", screen)

		else:  #pongdef1 == 1

			words(SCREEN_WIDTH*3/8, SCREEN_HEIGHT*2/5, BLACK, 50, "2-player", screen)


		words(SCREEN_WIDTH/8, SCREEN_HEIGHT*3/5, BLACK, 50, "[2]Type of game:", screen)


		#secret ingredient over here...
		pongdef2=pong2%3

		if pongdef2 == 2:

			words(SCREEN_WIDTH*3/8, SCREEN_HEIGHT*3/5, BLACK, 50, "Classic(11)", screen)

		elif pongdef2 == 1:

			words(SCREEN_WIDTH*3/8, SCREEN_HEIGHT*3/5, BLACK, 50, "First to reach 5", screen)

		else:  #pongdef2 == 0

			words(SCREEN_WIDTH*3/8, SCREEN_HEIGHT*3/5, BLACK, 50, "Random", screen)






		words(SCREEN_WIDTH*3/4, SCREEN_HEIGHT*1/7+15, BLACK, 60, "Instructions:", screen)


		if pongdef1==0:

			words(SCREEN_WIDTH*3/4, SCREEN_HEIGHT*2/5, BLACK, 50, "Use [Q]/[A] to move paddle", screen)


		else:

			words(SCREEN_WIDTH*3/4, SCREEN_HEIGHT*2/5, BLACK, 45, "Use [Q]/[A] and [P]/[L] to move paddle", screen)




		words(SCREEN_WIDTH*3/4, SCREEN_HEIGHT*3/5, BLACK, 50, "Press [Y] to pause", screen)



		words(SCREEN_WIDTH/2, SCREEN_HEIGHT*12/14, BLACK, 50, "Press [SPACE BAR] to continue", screen)



		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_1:
					pong1 += 1
				if event.key == pygame.K_2:
					pong2 += 1
				if event.key == pygame.K_3:
					done = True
				if event.key == pygame.K_SPACE:
					#here, from pongdef1(0/1)--->single(True/False) from pongdef2(0,1,2)--->style(1,2,3)(a eliminar)
					pongdef2 = pongdef2
					if pongdef1 == 0:
						single = True
					elif pongdef1 == 1:
						single = False
					ball.dir_x = ball.dir_x
					ball.dir_y = 0
					player_one.rect.y = SCREEN_HEIGHT//2-30
					player_two.rect.y = SCREEN_HEIGHT//2-30
					pause = False
					menu = False


	if  maxscore == 1 and menu == False:
		if pongdef2 == 0:
			maxscore = random.randint(3,8)
		if pongdef2 == 1:
			maxscore = 5
		if pongdef2 ==2:
			maxscore = 11
		print (maxscore)




	if menu == False: #animar e desenhar componentes gráficos (não texto) DEPOIS de escolher o tipo de jogo
		drawables_list.draw(screen)
		if pause == False:
			animated_list.update()
	#---------------------------------------------Pontuação--------------------------------
	if menu == False:
		if match == False: #se não for matchpoint

			words(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, CWALLS, 150, scoreTot, screen)


		elif match == True: #se for matchpoint

			words(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, RED, 150, scoreTot, screen)

		if pause == True:

			words(SCREEN_WIDTH/2, SCREEN_HEIGHT*2/3, CWALLS, 115, " Get     Ready", screen)

	#-----------------------Anúncio do campeão--------------------

	if winplayer != 0:
		if ball in animated_list: animated_list.remove(ball)
		if winplayer == 1:
			winstring = "Player 1 wins!"

		elif winplayer == 2:
			winstring = "Player 2 wins!"

	#-----------------1st- Player x wins
		screen.fill(CFUNDO)

		words(SCREEN_WIDTH/2, SCREEN_HEIGHT*4/15, CWALLS, 150, winstring, screen)

	#---------------Resultado final
		score1 = score1
		score2 = score2
		score_Tot = str(score1) + "-" + str(score2)

		words(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, CWALLS, 65, score_Tot, screen)


	#---------------Recomeçar?


		words(SCREEN_WIDTH/2, SCREEN_HEIGHT/2+75, CWALLS, 50, "Press [G] to restart, and [Y] for Menu", screen)





		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_g or event.key == pygame.K_h or event.key == pygame.K_y:
					player_one.kill()
					player_two.kill()
					score1 = 0
					score2 = 0
					scoreTot = str(score1) + "   " + str(score2)
					winplayer = 0
					ball.kill()
					ball = None
					match = False
					player = False
				if event.key == pygame.K_y:
					menu = True
				if event.key == pygame.K_b:
					done = True
			if event.type == pygame.QUIT:
				done = True



	# atualizar o ecrã com o conteúdo desenhado
	pygame.display.flip()
	# instruir o relógio que queremos no máximo x ciclos de atualização por segundo.
	# Desencadeará um tempo de espera apropriado para cumprir o objetivo
	clock.tick(FPS)

# Chega-se aqui quando done for True
pygame.quit()
