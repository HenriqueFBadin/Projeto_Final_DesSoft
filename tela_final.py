import pygame
from assets import *
QUIT=5
GAME=4
INIT=1
LEFT=1
RIGHT=3
state=0

player1_selecionou=False
player2_selecionou=False
def tela_final(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega o fundo da tela inicial
    background = pygame.image.load('Imagem/tela_final.png').convert()
    background= pygame.transform.scale(background,(WIDTH,HEIGHT))
    background_rect = background.get_rect()
    running = True
    while running:

        # Ajusta a velocidade do jogo.
        clock.tick(tick_rate)

        # Processa os eventos (mouse, teclado, botão, etc).
        event= pygame.event.poll()
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP and event.button == LEFT:
            if event.pos[0]>=234 and event.pos[0]<=515 and event.pos[1]>=464 and event.pos[1]<=508:
                return 1
            if event.pos[0]>=234 and event.pos[0]<=515 and event.pos[1]>=535 and event.pos[1]<=578:
                return 6
                # A cada loop, redesenha o fundo e os sprites
        screen.blit(background, background_rect)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
            
            