import random
import pygame
neg=-1
P1_WIDTH=150
P1_HEIGHT=150
WIDTH=800
HEIGHT=600
p1_shoot=False
p2_shoot=False

class Player(pygame.sprite.Sprite):
    def __init__(self, orientacao, imgs, img_weaks, all_sprites, all_powers, sprite_power, power_img, sprite_punch, punch_img, goldpunch_img, shoot_img, goldshot_img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.orientacao = orientacao
        self.imgs = imgs
        self.img_weaks = img_weaks
        self.image = imgs[orientacao]
        self.image_weak = img_weaks[orientacao]
        self.damage = 10
        self.rect = self.image.get_rect()
        self.rect.centerx = 50 if orientacao == 1 else WIDTH - 50
        self.rect.y = 400
        self.speedx = 0
        self.speedy = 0
        self.energy = 0
        self.punching_energy=0
        self.shooting_energy=0
        self.is_jumping = False
        self.is_punching = False
        self.is_shooting=False
        self.life=100
        self.all_sprites=all_sprites
        self.all_powers=all_powers
        self.sprite_power=sprite_power
        self.sprite_punch=sprite_punch
        self.power_img=power_img
        self.punch_img=punch_img
        self.goldpunch_img=goldpunch_img
        self.shoot_img=shoot_img
        self.goldshot_img=goldshot_img
        self.damage = 10

    def update(self):
        # Atualização da posição do player
        if self.is_jumping:
            self.energy += 1
        self.rect.x += self.speedx
        self.rect.y += self.energy
        if self.life <= 50:
            self.damage = 15
            self.image = self.image_weak

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

        if self.life>=50:
            self.image = self.imgs[self.orientacao]
            self.image_weak = self.img_weaks[self.orientacao]
        
        if self.is_punching and self.life>=50:
            self.punching_energy-=1
            self.image = self.punch_img[self.orientacao]
            if self.punching_energy<=0:
                self.is_punching=False

        if self.is_punching and self.life<50:
            self.punching_energy-=1
            self.image = self.goldpunch_img[self.orientacao]
            if self.punching_energy<=0:
                self.is_punching=False

        if self.is_shooting and self.life>=50:
            self.shooting_energy-=1
            self.image = self.shoot_img[self.orientacao]
            if self.shooting_energy<=0:
                self.is_shooting=False
        if self.is_shooting and self.life<50:
            self.shooting_energy-=1
            self.image = self.goldshot_img[self.orientacao]
            if self.shooting_energy<=0:
                self.is_shooting=False

    def jump(self):
        if not self.is_jumping:
            self.energy = -25
            self.is_jumping = True

    def shoot(self):

        self.is_shooting=True
        self.shooting_energy=12
        new_power=Power(self.orientacao, [self.power_img, self.power_img], self.rect.bottom-85, self.rect.centerx)
        self.all_sprites.add(new_power)
        self.all_powers.add(new_power)
        self.sprite_power.add(new_power)

    def punch(self):
        if not self.is_punching:
            self.punching_energy = 12
            self.is_punching=True

class Power(pygame.sprite.Sprite):

    # Construtor da classe:
        def __init__(self, orientacao, img, bottom, centerx):

            # Construtor da classe mãe (Sprite):
            pygame.sprite.Sprite.__init__(self)

            self.orientacao = orientacao
            self.image = img[orientacao]
            self.rect = self.image.get_rect()

            # Coloca no lugar inicial definido em x, y do constutor:
            self.rect.centerx = centerx
            self.rect.bottom = bottom
            self.speedx = -10  # Velocidade fixa para a horizontal]


        def update(self):
            
            # O poder só se move no eixo x:
            if self.orientacao==0:
                self.rect.centerx+=self.speedx
            if self.orientacao==1:
                self.rect.centerx-=self.speedx
              
            # Se o poder passar do inicio da tela, morre:
            if self.rect.centerx >  WIDTH or self.rect.centerx<0:
                self.kill()