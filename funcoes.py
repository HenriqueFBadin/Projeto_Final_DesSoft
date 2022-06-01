import pygame
pygame.init()
from assets import *

def texto(font, variavel, pos):
    text_surface = font.render("{}".format(variavel), True, (0, 0, 0))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (pos[0],  pos[1])
    window.blit(text_surface, (pos[0],  pos[1]))
    return 0

def tecla_pressionada(player1, player2, segundos):
    for event in pygame.event.get():
        # Verifica se apertou alguma tecla.
        if event.type == pygame.KEYDOWN:
# ----------Movimentação do player 2 (Setinhas):
            if event.key == pygame.K_LEFT:
                player2.orientacao = 0
                player2.speedx -= 8
            if event.key == pygame.K_RIGHT:
                player2.orientacao = 1
                player2.speedx += 8
            if event.key == pygame.K_UP:
                player2.jump()

# ----------Movimentação do player 1 (W,A,D):
            if event.key == pygame.K_a:
                player1.orientacao = 0
                player1.speedx -= 8
            if event.key == pygame.K_d:
                player1.orientacao = 1
                player1.speedx += 8
            if event.key==pygame.K_w:
                player1.jump()

# ----------Tiros (Q, L):            
            if event.key==pygame.K_q and player1.life > 0 and player1.segundostiro == 0:
                player1.shoot()
                player1.segundostiro = 64
            if event.key==pygame.K_l and player2.life > 0 and player2.segundostiro == 0:
                player2.shoot()
                player2.segundostiro = 64

# ----------Sprite do soco (E, <):
            if event.key == pygame.K_e and player1.segundossoco == 0:
                if player1.orientacao == 0:
                    player1.rect.x -= 30
                elif player1.orientacao == 1:
                    player1.rect.x += 30
                player1.punch()
                player1.segundossoco = 30
            if event.key == pygame.K_COMMA and player2.segundossoco == 0:
                if player2.orientacao == 0:
                    player2.rect.x -= 30
                elif player2.orientacao == 1:
                    player2.rect.x += 30
                player2.punch()
                player2.segundossoco = 30
                
        
        # Verifica se soltou alguma tecla.
        if event.type == pygame.KEYUP:
            # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_LEFT:
                player2.speedx += 8
            if event.key == pygame.K_RIGHT:
                player2.speedx -= 8
            if event.key == pygame.K_a:
                player1.speedx += 8
            if event.key == pygame.K_d:
                player1.speedx -= 8
            if event.key == pygame.K_UP:
                player2.jump()
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            pygame.quit()
    return True

def encostou(player1, player2):
    if player2.image in player2.punch_img or player2.image in player2.goldpunch_img:
        if player2.umsoco == 1:
            player1.life -= player2.damage
            player2.umsoco = 0
            player1.compbarraverd -= 5
    if player1.rect.centerx >= player2.rect.centerx:
        player1.rect.x += 30
    if player1.rect.centerx < player2.rect.centerx:
        player1.rect.x -= 30
    if player1.life<=0:            
        player1.kill()
    if player1.image in player1.punch_img or player1.image in player1.goldpunch_img:
        if player1.umsoco == 1:
            player2.life -= player1.damage
            player1.umsoco = 0
            player2.compbarraverd -= 5
    if player2.rect.centerx >= player1.rect.centerx:
        player2.rect.x += 30
    if player2.rect.centerx < player1.rect.centerx:
        player2.rect.x -= 30
    if player2.life<=0:
        player2.kill()
    return 0

def verificamorreu(player1, player2):
    if player1.life<=0:            
        player1.kill()
        player1.life = 0
    if player2.life<=0:
        player2.kill()
        player2.life = 0
    return 0

def contadorinicial(font,pos,all_sprites):
    valores = [3,2,1,0,'go',' ']
    for valor in valores:
        text_surface = font.render("{}".format(valor), True, (0, 0, 0))
        text_rect = text_surface.get_rect()
        text_rect.midtop = (pos[0],  pos[1])
        window.blit(text_surface, (pos[0],  pos[1]))
        all_sprites.draw(window)
    return 0