import pygame
pygame.init()
from assets import *
from funcoes import *
from game_screen import game_screen
from init_sceen import init_screen
from character_selection import character_selection
QUIT=5
MENU=3
GAME=4
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Mortal Insper!')
INIT=1
state=INIT
while state!= QUIT:
    if state==INIT:
        state=init_screen(window)
    elif state==MENU:
        state=character_selection(window)
    elif state==4:
        state=game_screen
    else:
        state=QUIT
pygame.quit()

'''elif state==GAME:
        state=character_selection(window)'''