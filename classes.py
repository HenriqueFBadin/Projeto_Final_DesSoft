import random
import pygame

P1_WIDTH=150
P1_HEIGHT=150
WIDTH=800
HEIGHT=600

class Player(pygame.sprite.Sprite):
    def __init__(self, img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH/2
        self.rect.y = 400
        self.speedx = 0
        self.speedy = 0
        self.energy = 0
        self.is_jumping = False
        self.life=100

    def update(self):
        # Atualização da posição do p1
        if self.is_jumping:
            self.energy += 1
        self.rect.x += self.speedx
        self.rect.y += self.energy

        # Mantem dentro da tela
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom < 0:
            self.rect.bottom = 0
        if self.rect.y > 400:
            self.rect.y = 400
            self.is_jumping = False
            self.energy = 0
    
    def jump(self):
        if not self.is_jumping:
            self.energy = -25
            self.is_jumping = True

