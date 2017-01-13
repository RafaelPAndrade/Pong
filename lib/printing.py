# printing.py, featuring words()
#	Attempt at function to easily write stuff, using pygame (for my games)
#by Rafael P.A.


import pygame

#x,y- place of center of the text
#color - obvious, using values from constants.py
#size - size of the characters, maybe in pixels?
#string - whatever you want to write in screen
#place - name of your screen in pygame, default "screen"


def words(x, y, color, size, string,place):
    font = pygame.font.Font(None, size)
    text = font.render(string, 9, color) #color may refer to the constants.py file
    textpos = text.get_rect()
    textpos.centerx = x
    textpos.centery = y
    place.blit(text, textpos)
    
    return True


