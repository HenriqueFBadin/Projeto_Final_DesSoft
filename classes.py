import random
import pygame

P1_WIDTH=10
P1_HEIGHT=10
WIDTH=1080
HEIGHT=1920

class p1(pygame.sprite.Sprite):
    def __init__(self, img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('Imagem/Quadrado_Teste.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (P1_WIDTH, P1_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0

    def update(self):
        # Atualização da posição do p1
        self.rect.x += self.speedx

        # Mantem dentro da tela
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0