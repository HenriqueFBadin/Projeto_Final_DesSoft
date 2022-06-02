import pygame
from funcoes import *

from assets import HEIGHT, WIDTH
FPS=64
QUIT=3
MENU=3
def init_screen(window):

    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega o fundo da tela inicial
    background = pygame.image.load('Imagem/Menu.png').convert()
    background= pygame.transform.scale(background,(WIDTH,HEIGHT))
    background_rect = background.get_rect()

    running = True
    while running:

        # Ajusta a velocidade do jogo.
        clock.tick(FPS)

        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = QUIT
                running = False

            if event.type == pygame.KEYUP:
                state = MENU
                running = False

      
        window.blit(background,background_rect)
        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return state