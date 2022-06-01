import pygame
pygame.init()
from assets import *
from main import game_screen
from init_sceen import init_screen
QUIT=5
GAME=3
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Mortal Insper!')
INIT=1
state=INIT
while state!= QUIT:
    if state==INIT:
        state=init_screen(window)
    elif state==GAME:
        state=game_screen(window)
    else:
        state=QUIT
pygame.quit()

