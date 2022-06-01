import pygame
from assets import *
QUIT=2
GAME=1
INIT=1
state=False
seta_esq_img=pygame.image.load('Setinha de selecao pra esquerda.png').convert()
seta_dir_img=pygame.image.load('Setinha de selecao pra direita.png').convert()
seta_esq_img=pygame.transform.scale(seta_esq_img(100,46))
seta_dir_img=pygame.transform.scale(seta_dir_img(100,46))

class Seta(pygame.sprite.Sprite):
    def _init_(self,img):
        pygame.sprite.Sprite._init_(self) 

        self.centerx=50
        self.rect.y=400
        self.img=img
        self.speedy=0
    def update(self):
        self.rect.y+=self.speedy
seta_esq=Seta(seta_esq_img)
seta_dir=Seta(seta_dir_img)
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
            if event.type == pygame.KEYUP:
                if event.type==pygame.K_w:
                    seta_esq.speedy+=50
                running = False

        # A cada loop, redesenha o fundo e os sprites
        screen.blit(background, background_rect)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return state
