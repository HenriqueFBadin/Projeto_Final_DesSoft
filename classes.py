import random
import pygame
from sympy import true

import pygame
neg=-1
P1_WIDTH=150
P1_HEIGHT=150
WIDTH=800
HEIGHT=600
p1_shoot=False
p2_shoot=False
class Power(pygame.sprite.Sprite):
    # Construtor da classe.
        def __init__(self, img, bottom, centerx):
            # Construtor da classe mãe (Sprite).
            pygame.sprite.Sprite.__init__(self)

            self.image = img
            self.rect = self.image.get_rect()

            # Coloca no lugar inicial definido em x, y do constutor
            self.rect.centerx = centerx
            self.rect.bottom = bottom
            self.speedx = -10  # Velocidade fixa para cima

        def update(self):
            # A bala só se move no eixo y
            self.rect.centerx-=self.speedx
              

            # Se o tiro passar do inicio da tela, morre.
            if self.rect.centerx >  WIDTH or self.rect.centerx<0:
                self.kill()
class Player(pygame.sprite.Sprite):
    def __init__(self, img, all_sprites,all_powers, power_img):
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
        self.is_punching = False
        self.life=100
        self.all_sprites=all_sprites
        self.all_powers=all_powers
        self.power_img=power_img
    def update(self):
        # Atualização da posição do player
        if self.is_jumping:
            self.energy += 1
        if self.is_punching:
            self.duracao -= 1
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

    def shoot(self):
        # A nova bala vai ser criada logo acima e no centro horizontal da nave
        new_power =Power(self.power_img, self.rect.bottom-70, self.rect.centerx)
        self.all_sprites.add(new_power)
        self.all_powers.add(new_power)