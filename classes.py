import random
import pygame

P1_WIDTH=150
P1_HEIGHT=150
WIDTH=1920
HEIGHT=1080

class p1(pygame.sprite.Sprite):
    def __init__(self, img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = 400
        self.rect.bottom = 970
        self.speedx = 0

    def update(self):
        # Atualização da posição do p1
        self.rect.x += self.speedx

        # Mantem dentro da tela
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0