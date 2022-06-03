import pygame
import os

pygame.init()
pygame.mixer.init()
from assets import *
from funcoes import *
from game_screen import game_screen
from init_sceen import init_screen

from character_selection import character_selection
QUIT=5
MENU=3
GAME=4
player1_esc=0
player2_esc=0
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Mortal Insper!')
INIT=1
state=INIT
while state!= QUIT:
    if state==INIT:

        state=init_screen(window)
    if state==MENU:
        state=character_selection(window)
        print(state)
        
    if state[0]==4:
        player1_esc=state[1]
        player2_esc=state[2]
        state=game_screen(window,player1_esc,player2_esc)
    if state!=INIT and state!=MENU and state[0]!=4:
        state=QUIT
pygame.quit()
