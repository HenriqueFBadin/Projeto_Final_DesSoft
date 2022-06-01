import pygame
from assets import *
QUIT=2
GAME=3
INIT=1
player1_selecionou=False
player2_selecionou=False
state=1
all_setas = pygame.sprite.Group()
seta_esq_img=pygame.image.load('Imagem/Setinha de selecao pra esquerda.png').convert_alpha()
seta_dir_img=pygame.image.load('Imagem/Setinha de selecao.png').convert_alpha()
seta_esq_img=pygame.transform.scale(seta_esq_img,(100,46))
seta_dir_img=pygame.transform.scale(seta_dir_img,(100,46))

class Seta(pygame.sprite.Sprite):
    def _init_(self,all_setas,img):
        pygame.sprite.Sprite._init_(self,all_setas,img) 

        self.centerx=50
        self.rect.y=400
        self.all_setas=all_setas
        self.img=img
        self.speedy=0
    def update(self):
        self.rect.y+=self.speedy
        if self.rect.y > 400:
            self.rect.y = 400
seta_esq=Seta(all_setas,seta_esq_img)
seta_dir=Seta(all_setas,seta_dir_img)
all_setas.add(seta_esq)
all_setas.add(seta_dir)
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
                    seta_esq.speedy-=50
                if event.type==pygame.K_s:
                    seta_esq.speedy+=50
                if event.type==pygame.K_UP:
                    seta_dir.speedy-=50
                if event.type==pygame.K_DOWN:
                    seta_dir.speedy+=50
                 
                if event.type==pygame.K_e:
                    player1_selecionou=True
                if event.type==pygame.K_COMMA:
                    player2_selecionou=True
            if player1_selecionou and player2_selecionou:
                state=2
                running = False

        # A cada loop, redesenha o fundo e os sprites
        screen.blit(background, background_rect)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return state
