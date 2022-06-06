from turtle import circle
import pygame
from assets import *
QUIT=5
GAME=4
INIT=1
LEFT=1
RIGHT=3

player1_selecionou=False
player2_selecionou=False
def character_selection(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega o fundo da tela inicial
    background = pygame.image.load('Imagem/Champion_Select.png').convert()
    background= pygame.transform.scale(background,(WIDTH,HEIGHT))
    background_rect = background.get_rect()
    player1_selecionou=False
    player2_selecionou=False
    running = True
    p1c=0
    p2c=0
    segundos4=64
    timer3=0
    GREEN=(0,255,0)

    #triangle1=pygame.Rect((80,81),(180,81),(130,138))
    while running:

        # Ajusta a velocidade do jogo.
        clock.tick(tick_rate)

        # Processa os eventos (mouse, teclado, botão, etc).
        event= pygame.event.poll()
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP and event.button == LEFT:
            if event.pos[0]>=124 and event.pos[0]<=226 and event.pos[1]>=75 and event.pos[1]<=170:
                print("P1 escolheu o lobisomen")
                p1c=2
                player1_selecionou=True
                x1=[[52,102],[52,178],[106,141]]               
                
            if event.pos[0]>=124 and event.pos[0]<=226 and event.pos[1]>=177 and event.pos[1]<=273:
                print("P1 escolheu o Dio")
                p1c=1
                player1_selecionou=True
                x1=[[52,222],[52,306],[101,262]]
            if event.pos[0]>=124 and event.pos[0]<=226 and event.pos[1]>=278 and event.pos[1]<=373:
                print("P1 escolheu o Honda")
                p1c=4 #mudar para 4, quando o Honda estiver pronto
                player1_selecionou=True
                x1=[[52,349],[52,438],[106,390]]
            if event.pos[0]>=124 and event.pos[0]<=226 and event.pos[1]>=379 and event.pos[1]<=474:
                print("P1 escolheu o Humberto")
                p1c=3
                player1_selecionou=True
                x1=[[52,482],[52,554],[102,520]]
            if event.pos[0]>=124 and event.pos[0]<=226 and event.pos[1]>=480 and event.pos[1]<=578:
                print("P1 escolheu o Yoshi")
                p1c=5
                player1_selecionou=True
                x1=[[52,482],[52,554],[102,520]]
            if event.pos[0]>=603 and event.pos[0]<=706 and event.pos[1]>=74 and event.pos[1]<=172:
                print("P2 escolheu o lobisomen")
                p2c=2
                player2_selecionou=True
                x2=[[694,140],[747,106],[747,186]]
            if event.pos[0]>=603 and event.pos[0]<=706 and event.pos[1]>=176 and event.pos[1]<=273:
                print("P2 escolheu o Dio")
                p2c=1
                player2_selecionou=True
                x2=[[694,264],[747,218],[747,309]]
            if event.pos[0]>=603 and event.pos[0]<=706 and event.pos[1]>=277 and event.pos[1]<=374:
                print("P2 escolheu o Honda")
                p2c=4 
                player2_selecionou=True
                x2=[[694,393],[747,350],[747,443]]
            if event.pos[0]>=603 and event.pos[0]<=706 and event.pos[1]>=378 and event.pos[1]<=474:
                print("P2 escolheu o Humberto")
                p2c=3
                player2_selecionou=True
                x2=[[694,516],[747,468],[747,563]]
            if event.pos[0]>=603 and event.pos[0]<=706 and event.pos[1]>=478 and event.pos[1]<=578:
                print("P2 escolheu o Yoshi")
                p2c=5
                player2_selecionou=True
                x2=[[52,482],[52,554],[102,520]]
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == RIGHT:
            print ("(%d, %d)" % event.pos)
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == RIGHT:
            print ("(%d, %d)" % event.pos)
        elif player1_selecionou and player2_selecionou:
            state=GAME
            segundos4 -= 1
            if segundos4<=0:
                running=False


                


        # A cada loop, redesenha o fundo e os sprites
        screen.blit(background, background_rect)

        # Depois de desenhar tudo, inverte o display.
        if player1_selecionou==True:
            pygame.draw.polygon(screen,GREEN,x1)
        if player2_selecionou==True:
            pygame.draw.polygon(screen,GREEN,x2)
        pygame.display.flip()
     
      
   
    return [state,p1c,p2c] 
