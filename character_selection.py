import pygame
from assets import *
QUIT=2
GAME=3
INIT=1
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

    running = True
    while running:

        # Ajusta a velocidade do jogo.
        clock.tick(tick_rate)

        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            if event==pygame.quit:
                pygame.quit()        
            if event==pygame.MOUSEMOTION:
                if event==pygame.MOUSEBUTTONDOWN:
                    #mouse_pousition=pygame.mouse.get.pos()
                    running=False


        # A cada loop, redesenha o fundo e os sprites
        screen.blit(background, background_rect)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
        state=4
      

    return state
