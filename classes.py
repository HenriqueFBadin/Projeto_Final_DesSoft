import pygame
from assets import *

neg=-1
P1_WIDTH=150
P1_HEIGHT=150
WIDTH=800
HEIGHT=600
p1_shoot=False
p2_shoot=False

class Player(pygame.sprite.Sprite):
    def __init__(self, orientacao, all_sprites, all_powers, sprite_power, sprite_punch, power_img, imgs, img_weaks, punch_img, goldpunch_img, shoot_img, goldshot_img, jump_img, goldjump_img):
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
        self.life=200
        self.all_sprites=all_sprites
        self.all_powers=all_powers
        self.sprite_power=sprite_power
        self.sprite_punch=sprite_punch
        self.power_img=power_img
        self.punch_img=punch_img
        self.goldpunch_img=goldpunch_img
        self.shoot_img=shoot_img
        self.goldshot_img=goldshot_img
        self.jump_img=jump_img
        self.goldjump_img=goldjump_img
        self.damage = 10
        self.mask = pygame.mask.from_surface(self.image)
        self.mask_weak = pygame.mask.from_surface(self.image_weak)
        self.segundostiro = 0
        self.segundossoco = 0
        self.umsoco = 1
        self.morreu = 0
        self.escolha = 0

    def update(self):
        # Atualização da posição do player
        if self.speedx >= 13:
            self.speedx = 12
        if self.speedx <= -13:
            self.speedx = -12
        if self.speedx == 4 or self.speedx == -4:
            self.speedx = 0
        self.rect.x += self.speedx
        self.rect.y += self.energy
        if self.segundostiro > 0:
            self.segundostiro -= 1
        if self.segundossoco > 0:
            self.segundossoco -= 1

        if self.life < 100:
            self.damage = 15
            self.image = self.img_weaks[self.orientacao]

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

        # Rotaciona o personagem caso ele mude de direção
        if self.life>=100:
            self.image = self.imgs[self.orientacao]
            self.image_weak = self.img_weaks[self.orientacao]
        
        # Duração do soco e evita que o jogador cause dano mais de uma vez por soco
        if self.is_punching and self.life>=100:
            self.punching_energy-=1
            self.image = self.punch_img[self.orientacao]
            if self.punching_energy<=0:
                self.is_punching=False

        if self.is_punching and self.life<100:
            self.punching_energy-=1
            self.image = self.goldpunch_img[self.orientacao]
            if self.punching_energy<=0:
                self.is_punching=False

        # Duração do tiro
        if self.is_shooting and self.life>=100:
            self.shooting_energy-=1
            self.image = self.shoot_img[self.orientacao]
            if self.shooting_energy<=0:
                self.is_shooting=False

        if self.is_shooting and self.life<100:
            self.shooting_energy-=1
            self.image = self.goldshot_img[self.orientacao]
            if self.shooting_energy<=0:
                self.is_shooting=False

        # Duração do pulo
        if self.is_jumping and self.life>=100:
            self.energy+=1
            self.image = self.jump_img[self.orientacao]

        if self.is_jumping and self.life<100:
            self.energy+=1
            self.image = self.goldjump_img[self.orientacao]
        
        # Atualiza a máscara dos personagens, para aprimorar as colisões
        self.mask = pygame.mask.from_surface(self.image)
        self.mask_weak = pygame.mask.from_surface(self.image_weak)

        # Mata o jogador caso ele fica com a vida menor ou igual a 0
        if self.life<=0:           
            self.kill()
            self.life = 0
            self.morreu += 1


    def jump(self):
        if not self.is_jumping:
            self.energy = -25
            self.is_jumping = True

    def shoot(self):

        self.is_shooting=True
        self.shooting_energy=12
        if self.escolha == 7 and self.life < 100:
            self.power_img[self.orientacao]=pygame.transform.scale(self.power_img[self.orientacao],(140,140))
            self.rect.bottom = self.rect.bottom+50
        elif self.escolha == 7 and self.life >= 100:
            self.power_img[self.orientacao]=pygame.transform.scale(self.power_img[self.orientacao],(70,70))
            self.rect.bottom = self.rect.bottom+50
        new_power=Power(self.orientacao, self.power_img, self.rect.bottom-85, self.rect.centerx)
        self.all_sprites.add(new_power)
        self.all_powers.add(new_power)
        self.sprite_power.add(new_power)

    def punch(self):
        if not self.is_punching:
            self.punching_energy = 12
            self.is_punching=True

class Power(pygame.sprite.Sprite):
    """ Classe para configurar os disparos/tiros """
    # Construtor da classe:
    def __init__(self, orientacao, img, bottom, centerx):

        # Construtor da classe mãe (Sprite):
        pygame.sprite.Sprite.__init__(self)

        self.orientacao = orientacao
        self.image = img[orientacao]
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

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

class BarraHp(pygame.sprite.Sprite):
    """ Classe para configurar as barras de vida dos players """
    def __init__(self, playerlife, jogador, barravermelha_img, barraverde_img):
        self.compbarraverd = 300
        self.compbarraverm = 300
        self.playerlife = playerlife
        self.jogador = jogador
        self.barravermelha_img = pygame.transform.scale(barravermelha_img, (self.compbarraverm, 40))
        self.barraverde_img = pygame.transform.scale(barraverde_img, (self.compbarraverd, 40))      
    def update(self):
        if self.playerlife > 100:
            self.barraverde_img = pygame.transform.scale(self.barraverde_img, (self.compbarraverd, 40))
        else:
            self.barravermelha_img = pygame.transform.scale(self.barravermelha_img, (self.compbarraverm, 40))

        