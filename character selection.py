import pygame
from assets import *
QUIT=2
GAME=1
INIT=1
seta_esq=pygame.image.load('Setinha de selecao pra esquerda.png').convert()
seta_dir=pygame.image.load('Setinha de selecao pra direita.png').convert()
seta_esq=pygame.transform.scale(seta_esq(100,46))
seta_dir=pygame.transform.scale(seta_dir(100,46))
class Seta(pygame.sprite.Sprite):
    def _init_(self,orientacao,img):
        pygame.sprite.Sprite._init_(self) 
        self.orientacao=orientacao
        self.centerx=50
        self.img=img
def character_selection(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega o fundo da tela inicial
    background = pygame.image.load('character selection menu.png').convert()
    background_rect = background.get_rect()

    running = True
    while running:

        # Ajusta a velocidade do jogo.
        clock.tick(tick_rate)

        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = QUIT
                running = False

            if event.type == pygame.KEYUP:
                state = GAME
                running = False

        # A cada loop, redesenha o fundo e os sprites
        screen.blit(background, background_rect)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return state
