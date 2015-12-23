#coding: utf-8


import pygame
import random
from block import Block

from paddle import Paddle
from wall import Wall
from ball import Ball

import constants



# Inicializao da biblioteca pygame
pygame.init()

# Criação da janela com a resolução indicada
screen = pygame.display.set_mode([constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT])

# Definição do título da janela
pygame.display.set_caption('Pong')



# inicializar o relógio
clock = pygame.time.Clock()


# variável usada para assinalar que o jogo terminou
done = False

# criar a(s) raquete(s)


# criar as paredes
top_wall = Wall(0,0,constants.SCREEN_WIDTH,constants.CWALLS)
bottom_wall = Wall(0,constants.SCREEN_HEIGHT-15,constants.SCREEN_WIDTH,constants.CWALLS)

#todo -paredes
walls_list = pygame.sprite.Group()

walls_list.add(top_wall)
walls_list.add(bottom_wall)


#todo

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

# adicionar a(s) raquete(s) à lista de objetos que colidem com a bola


# adicionar os objetos que necessitam ser desenhados
drawables_list.add(top_wall)
drawables_list.add(bottom_wall)

# criar a rede e adicionar os objetos à lista de objetos que necessitam ser redesenhados
for i in range(0,constants.SCREEN_HEIGHT,30):
	net = Block(constants.SCREEN_WIDTH//2-7,i+15,14,15,constants.CWALLS)
	drawables_list.add(net)

# adicionar a(s) raqueta(s)


# adicionar os objetos que necessitam ser atualizados à lista respetiva


#---------coisas:tipo de jogo, pontuações, o resultado para ganhar, cores--------------------
style =	0 					#tipo de jogo
score1 = 0 					#score player 1
score2 = 0					#score player 2
winplayer = 0					#que jogador ganhou
scoreTot = str(score1) + "   " + str(score2) 	#string que comporta o score
maxscore = 1					#pontos máximos (até aos maxscore pontos) 
match =	False					
single = False
pause = False
pong1 = 2
pong2 = 3

#------------------------------ciclo principal---------------------------------------------
while not done:
	
	
	
	if match == False: 
		Height1 = constants.Height1
		Height2 = constants.Height2	
	elif match == True:	
		if score1 >= score2:
			Height1 = constants.Height1*2/3
		if score2 >= score1:
			Height2 = constants.Height2*2/3

	
	
	if player == False:
		if match == False:	
			

			player_one = Paddle(30,constants.SCREEN_HEIGHT//2-30,Height1,constants.CPLAYER1)
			player_two = Paddle(constants.SCREEN_WIDTH-30-15,constants.SCREEN_HEIGHT//2-30,Height2,constants.CPLAYER2)		
			
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
			
			
			player_one = Paddle(30,constants.SCREEN_HEIGHT//2-30,Height1,constants.CPLAYER1)
			player_two = Paddle(constants.SCREEN_WIDTH-30-15,constants.SCREEN_HEIGHT//2-30,Height2,constants.CPLAYER2)		
			
			player_one.set_walls(walls_list)
			player_two.set_walls(walls_list)		
			colliders_list.add(player_one)
			colliders_list.add(player_two)		
			drawables_list.add(player_one)
			drawables_list.add(player_two)		
			animated_list.add(player_one)
			animated_list.add(player_two)	
			player = True	
	
	
	
	
	# Verificar se é necessário criar uma nova bola e players?
	if ball == None:
		ball = Ball(constants.SCREEN_WIDTH//2-7,constants.SCREEN_HEIGHT//2-7,constants.CBALL)
		ball.set_colliders(colliders_list)
		# adicionar a bola à lista de objetos a atualizar
		animated_list.add(ball)
		drawables_list.add(ball)
		
		if score1 == 0 and score2 == 0:
			ball.dir_x = ball.dir_x
			ball.dir_y = 0
			player_one.rect.y = constants.SCREEN_HEIGHT//2-30
			player_two.rect.y = constants.SCREEN_HEIGHT//2-30

	

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
	"""--------------------------------------------- A lógica do jogo ----------------------------------------"""
	
	# Testar se a bola sai pela esquerda (ponto para o jogador 2)
		#Ponto para o jogador 2
	if ball.rect.x < - 10 or ball.rect.x > constants.SCREEN_WIDTH + 10 :
		if ball.rect.x < -10 :
			score2 += 1 
			scoreTot = str(score1) + "   " + str(score2)
			print(scoreTot)
			ball.kill()
			ball = None
			
			
		#Ponto para o jogador 1
		elif ball.rect.x > constants.SCREEN_WIDTH + 10 :
			score1 += 1
			scoreTot = str(score1) + "   " + str(score2)
			print(scoreTot)		
			ball.kill()
			ball = None
		
		
#-------------------MatchPoint---------------------------
		
		#estilo 2 ou 1
		if style == 2 or style ==1:
			if score1+1 >= maxscore:
				match = True
				player = False

			elif score2+1 >= maxscore:
				match = True
				player = False
		
		#estilo 3
		if style == 3:
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
		
		if score1 >= maxscore and style != 3:
			winplayer = 1
		elif score2 >= maxscore and style != 3:
			winplayer = 2
					
		#Existem capotes...
		if style == 3:
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
	screen.fill(constants.CFUNDO)
	# desenhar tudo o que é visível 	# Display some text
	
	
	
	#-----------------Intro---------------------
	
		
	if style == 0:
		font = pygame.font.Font(None, 70)
		text = font.render("PONG", 1, constants.BLACK)
		textpos = text.get_rect()
		textpos.centerx = constants.SCREEN_WIDTH/2
		textpos.centery = constants.SCREEN_HEIGHT*1/14
		screen.blit(text, textpos)		
		
		font = pygame.font.Font(None, 60)
		text = font.render("Options:", 1, constants.BLACK)
		textpos = text.get_rect()
		textpos.centerx = constants.SCREEN_WIDTH/4
		textpos.centery = constants.SCREEN_HEIGHT*1/7+15
		screen.blit(text, textpos)	
		
		font = pygame.font.Font(None, 30)
		text = font.render("(Use numbers to toggle)", 1, constants.BLACK)
		textpos = text.get_rect()
		textpos.centerx = constants.SCREEN_WIDTH/4
		textpos.centery = constants.SCREEN_HEIGHT*1/7+30+15
		screen.blit(text, textpos)
		
		font = pygame.font.Font(None, 50)
		text = font.render("[1]N Players:", 1, constants.BLACK)
		textpos = text.get_rect()
		textpos.centerx = constants.SCREEN_WIDTH/8
		textpos.centery = constants.SCREEN_HEIGHT*2/5
		screen.blit(text, textpos)
		
		pongdef1=pong1%2

		if pongdef1== 0:

			text = font.render("Single-player", 1, constants.BLACK)
			textpos = text.get_rect()
			textpos.centerx = constants.SCREEN_WIDTH*3/8
			textpos.centery = constants.SCREEN_HEIGHT*2/5
			screen.blit(text, textpos)
		else:	

			text = font.render("2-player", 1, constants.BLACK)
			textpos = text.get_rect()
			textpos.centerx = constants.SCREEN_WIDTH*3/8
			textpos.centery = constants.SCREEN_HEIGHT*2/5
			screen.blit(text, textpos)
		
		
		
		font = pygame.font.Font(None, 50)
		text = font.render("[2]Type of game:", 1, constants.BLACK)
		textpos = text.get_rect()
		textpos.centerx = constants.SCREEN_WIDTH/8
		textpos.centery = constants.SCREEN_HEIGHT*3/5
		screen.blit(text, textpos)		
		
		pongdef2=pong2%3
		
		if pongdef2== 2:
			
			font = pygame.font.Font(None, 50)
			text = font.render("Classic(11)", 1, constants.BLACK)
			textpos = text.get_rect()
			textpos.centerx = constants.SCREEN_WIDTH*3/8
			textpos.centery = constants.SCREEN_HEIGHT*3/5
			screen.blit(text, textpos)
		elif pongdef2== 1:
		
			font = pygame.font.Font(None, 50)
			text = font.render("First to reach 5", 1, constants.BLACK)
			textpos = text.get_rect()
			textpos.centerx = constants.SCREEN_WIDTH*3/8
			textpos.centery = constants.SCREEN_HEIGHT*3/5
			screen.blit(text, textpos)		
		else:
			
			font = pygame.font.Font(None, 50)
			text = font.render("Random", 1, constants.BLACK)
			textpos = text.get_rect()
			textpos.centerx = constants.SCREEN_WIDTH*3/8
			textpos.centery = constants.SCREEN_HEIGHT*3/5
			screen.blit(text, textpos)		

		
		
		
		
		font = pygame.font.Font(None, 60)
		text = font.render("Instructions:", 1, constants.BLACK)
		textpos = text.get_rect()
		textpos.centerx = constants.SCREEN_WIDTH*3/4
		textpos.centery = constants.SCREEN_HEIGHT*1/7+15
		screen.blit(text, textpos)		
	
		
		if pongdef1==0:
			
			font = pygame.font.Font(None, 50)
			text = font.render("Use Q/A to move paddle", 1, constants.BLACK)
			textpos = text.get_rect()
			textpos.centerx = constants.SCREEN_WIDTH*3/4
			textpos.centery = constants.SCREEN_HEIGHT*2/5
			screen.blit(text, textpos)
			
		else:
			font = pygame.font.Font(None, 45)
			text = font.render("Use [Q]/[A] and [P]/[L] to move paddle", 1, constants.BLACK)
			textpos = text.get_rect()
			textpos.centerx = constants.SCREEN_WIDTH*3/4
			textpos.centery = constants.SCREEN_HEIGHT*2/5
			screen.blit(text, textpos)
			
		font = pygame.font.Font(None, 50)
		text = font.render("Use [Y] to pause", 1, constants.BLACK)
		textpos = text.get_rect()
		textpos.centerx = constants.SCREEN_WIDTH*3/4
		textpos.centery = constants.SCREEN_HEIGHT*3/5
		screen.blit(text, textpos)
				
			
		font = pygame.font.Font(None, 50)
		text = font.render("Press [SPACE BAR] to continue", 1, constants.BLACK)
		textpos = text.get_rect()
		textpos.centerx = constants.SCREEN_WIDTH/2
		textpos.centery = constants.SCREEN_HEIGHT*12/14
		screen.blit(text, textpos)		

		
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
					style = pongdef2+1
					if pongdef1 == 0:
						single = True
					ball.dir_x = ball.dir_x
					ball.dir_y = 0
					player_one.rect.y = constants.SCREEN_HEIGHT//2-30
					player_two.rect.y = constants.SCREEN_HEIGHT//2-30
					pause = False					
		
	if style == 1:
		maxscore = random.randint(3,8)
	elif style ==2:
		maxscore = 5
	elif style == 3:
		maxscore = 11
		print(style)
									
	if style != 0: #animar e desenhar DEPOIS de escolher o tipo de jogo
		drawables_list.draw(screen)
		if pause == False:
			animated_list.update()
	#---------------------------------------------Pontuação--------------------------------
	if style != 0: 
		if match == False: #se não for matchpoint
			font = pygame.font.Font(None, 150)
			scoreTot = str(score1) + "   " + str(score2)
			text = font.render(scoreTot, 1, constants.CWALLS)
			textpos = text.get_rect()
			textpos.centerx = constants.SCREEN_WIDTH/2
			textpos.centery = constants.SCREEN_HEIGHT/2
			screen.blit(text, textpos)		
		elif match == True: #se for matchpoint
			font = pygame.font.Font(None, 150)
			scoreTot = str(score1) + "   " + str(score2)
			text = font.render(scoreTot, 1, constants.RED)
			textpos = text.get_rect()
			textpos.centerx = constants.SCREEN_WIDTH/2
			textpos.centery = constants.SCREEN_HEIGHT/2
			screen.blit(text, textpos)				
		
		
		if pause == True:
			font = pygame.font.Font(None, 115)
			text = font.render(" Get     Ready", 1, constants.CWALLS)
			textpos = text.get_rect()
			textpos.centerx = constants.SCREEN_WIDTH/2
			textpos.centery = constants.SCREEN_HEIGHT*2/3
			screen.blit(text, textpos)			
			
	#-----------------------Anúncio do campeão--------------------
	
	if winplayer != 0 and style != 0:
		if ball in animated_list: animated_list.remove(ball)
		if winplayer == 1:			
			winstring = "Player 1 wins!"
			
		elif winplayer == 2:
			winstring = "Player 2 wins!"

	#-----------------1st- Player x wins	
		screen.fill(constants.CFUNDO)
		font = pygame.font.Font(None, 150)
		text = font.render(winstring, 1, constants.CWALLS)
		textpos = text.get_rect()
		textpos.centerx = constants.SCREEN_WIDTH/2
		textpos.centery = constants.SCREEN_HEIGHT*4/15
		screen.blit(text, textpos)			
		
	#---------------Resultado final	
		score1 = score1
		score2 = score2
		score_Tot = str(score1) + "-" + str(score2)
		font = pygame.font.Font(None, 65)
		text = font.render(score_Tot, 1, constants.CWALLS)
		textpos = text.get_rect()
		textpos.centerx = constants.SCREEN_WIDTH /2 
		textpos.centery = (constants.SCREEN_HEIGHT)/2
		screen.blit(text, textpos)			
	
	
	#---------------Recomeçar?		
		font = pygame.font.Font(None, 50)
		text = font.render("Press [G] to restart, and [Y] for Menu", 1, constants.CWALLS)
		textpos = text.get_rect()
		textpos.centerx = constants.SCREEN_WIDTH /2 
		textpos.centery = (constants.SCREEN_HEIGHT)/2 + 75
		screen.blit(text, textpos)
		
		
		
		
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_g or event.key == pygame.K_h or event.key == pygame.K_y:
					score1 = 0
					score2 = 0
					scoreTot = str(score1) + "   " + str(score2)
					winplayer = 0
					player_one.rect.y = constants.SCREEN_HEIGHT//2-30
					player_two.rect.y = constants.SCREEN_HEIGHT//2-30
					ball = None
					match = False
					player_one.kill()
					player_two.kill()					
					player = False
				if event.key == pygame.K_y:
					style = 0
				if event.key == pygame.K_b:
					done = True
			if event.type == pygame.QUIT:
				done = True
					

	
	# atualizar o ecrã com o conteúdo desenhado
	pygame.display.flip()
	# instruir o relógio que queremos no máximo x ciclos de atualização por segundo. 
	# Desencadeará um tempo de espera apropriado para cumprir o objetivo
	clock.tick(constants.FPS)

# Chega-se aqui quando done for True
pygame.quit()
