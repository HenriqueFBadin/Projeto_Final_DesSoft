import pygame
from assets import *
QUIT=5
GAME=4
INIT=1
LEFT=1
RIGHT=3

state=1
player1_selecionou=False
player2_selecionou=False
def character_selection(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega o fundo da tela inicial
    background = pygame.image.load('Imagem/character selection menu.png').convert()
    background= pygame.transform.scale(background,(WIDTH,HEIGHT))
    background_rect = background.get_rect()
    player1_selecionou=False
    player2_selecionou=False
    running = True
    p1c=0
    p2c=0
    while running:

        # Ajusta a velocidade do jogo.
        clock.tick(tick_rate)

        # Processa os eventos (mouse, teclado, botão, etc).
        event= pygame.event.poll()
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP and event.button == LEFT:
            if event.pos[0]>=112 and event.pos[0]<=230 and event.pos[1]>=81 and event.pos[1]<=195:
                print("P1 escolheu o lobisomen")
                p1c=2
                player1_selecionou=True
            if event.pos[0]>=111 and event.pos[0]<=230 and event.pos[1]>=208 and event.pos[1]<=322:
                print("P1 escolheu o Dio")
                p1c=1
                player1_selecionou=True
            if event.pos[0]>=111 and event.pos[0]<=230 and event.pos[1]>=335 and event.pos[1]<=449:
                print("P1 escolheu o Honda")
                p1c=1 #mudar para 4, quando o Honda estiver pronto
                player1_selecionou=True
            if event.pos[0]>=111 and event.pos[0]<=230 and event.pos[1]>=462 and event.pos[1]<=576:
                print("P1 escolheu o Humberto")
                p1c=3
                player1_selecionou=True
            if event.pos[0]>=563 and event.pos[0]<=685 and event.pos[1]>=81 and event.pos[1]<=195:
                print("P2 escolheu o lobisomen")
                p2c=2
                player2_selecionou=True
            if event.pos[0]>=563 and event.pos[0]<=685 and event.pos[1]>=208 and event.pos[1]<=322:
                print("P2 escolheu o Dio")
                p2c=1
                player2_selecionou=True
            if event.pos[0]>=563 and event.pos[0]<=685 and event.pos[1]>=335 and event.pos[1]<=449:
                print("P2 escolheu o Honda")
                p2c=1 #mudar para 4 dps que o honda estiver pronto
                player2_selecionou=True
            if event.pos[0]>=563 and event.pos[0]<=685 and event.pos[1]>=462 and event.pos[1]<=576:
                print("P2 escolheu o Humberto")
                p2c=3
                player2_selecionou=True
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == RIGHT:
            print ("(%d, %d)" % event.pos)
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == RIGHT:
            print ("(%d, %d)" % event.pos)
        elif player1_selecionou and player2_selecionou:
            state=GAME
            running=False


                


        # A cada loop, redesenha o fundo e os sprites
        screen.blit(background, background_rect)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
     
      
   
    return state 
