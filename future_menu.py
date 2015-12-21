#coding: utf-8

import pygame


pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode([140, 600])

drawables_list = pygame.sprite.Group()

done = False

pong1 = 2
pong2 = 2
pong3 = 2
pong4 = 2

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_4:
				pong4 = pong4+1
			if event.key == pygame.K_1:
				pong1 = pong1+1		
			if event.key == pygame.K_2:
				pong2 = pong2+1
			if event.key == pygame.K_3:
				pong3 = pong3+1		
	
	
	
	
	#advantage-unlimited number of options(3,4,5,...)
	
	pongcon1=pong1%2
	pongcon2=pong2%2
	pongcon3=pong3%2
	pongcon4=pong4%2
	
	
	
	
	
	
	
	
			
	screen.fill([255,255,255])		
	
	
	
	
	font = pygame.font.Font(None, 30)
	text = font.render("[1]PONG:", 1, [0,0,0])
	textpos = text.get_rect()
	textpos.centerx = 120/4+15
	textpos.centery = 600/7*1
	screen.blit(text, textpos)	
	
	font = pygame.font.Font(None, 30)
	text = font.render("[2]PONG:", 1, [0,0,0])
	textpos = text.get_rect()
	textpos.centerx = 120/4+15
	textpos.centery = 600/7*2
	screen.blit(text, textpos)	
	
	font = pygame.font.Font(None, 30)
	text = font.render("[3]PONG:", 1, [0,0,0])
	textpos = text.get_rect()
	textpos.centerx = 120/4+15
	textpos.centery = 600/7*3
	screen.blit(text, textpos)		
	
	
	
	font = pygame.font.Font(None, 30)
	text = font.render("[4]PONG:", 1, [0,0,0])
	textpos = text.get_rect()
	textpos.centerx = 120/4+15
	textpos.centery = 600/7*4
	screen.blit(text, textpos)
	
	
	if pongcon1 == 0:
		font = pygame.font.Font(None, 30)
		text = font.render("true", 1, [0,0,0])
		textpos = text.get_rect()
		textpos.centerx = 120*3/4+20
		textpos.centery = 600/7*1
		screen.blit(text, textpos)		
	elif pongcon1 == 1:
		font = pygame.font.Font(None, 30)
		text = font.render("false", 1, [0,0,0])
		textpos = text.get_rect()
		textpos.centerx = 120*3/4+23
		textpos.centery = 600/7*1
		screen.blit(text, textpos)		

	if pongcon2 == 0:
		font = pygame.font.Font(None, 30)
		text = font.render("true", 1, [0,0,0])
		textpos = text.get_rect()
		textpos.centerx = 120*3/4+20
		textpos.centery = 600/7*2
		screen.blit(text, textpos)		
	elif pongcon2 == 1:
		font = pygame.font.Font(None, 30)
		text = font.render("false", 1, [0,0,0])
		textpos = text.get_rect()
		textpos.centerx = 120*3/4+23
		textpos.centery = 600/7*2
		screen.blit(text, textpos)		

	if pongcon3 == 0:
		font = pygame.font.Font(None, 30)
		text = font.render("true", 1, [0,0,0])
		textpos = text.get_rect()
		textpos.centerx = 120*3/4+20
		textpos.centery = 600/7*3
		screen.blit(text, textpos)		
	elif pongcon3 == 1:
		font = pygame.font.Font(None, 30)
		text = font.render("false", 1, [0,0,0])
		textpos = text.get_rect()
		textpos.centerx = 120*3/4+23
		textpos.centery = 600/7*3
		screen.blit(text, textpos)		

	
	if pongcon4 == 0:
		font = pygame.font.Font(None, 30)
		text = font.render("true", 1, [0,0,0])
		textpos = text.get_rect()
		textpos.centerx = 120*3/4+20
		textpos.centery = 600/7*4
		screen.blit(text, textpos)		
	elif pongcon4 == 1:
		font = pygame.font.Font(None, 30)
		text = font.render("false", 1, [0,0,0])
		textpos = text.get_rect()
		textpos.centerx = 120*3/4+23
		textpos.centery = 600/7*4
		screen.blit(text, textpos)		
		

	drawables_list.draw(screen)

	pygame.display.flip()

	clock.tick(120)

pygame.quit()
