import pygame
pygame.init()
from os import path
from assets import *

def texto(font, variavel, pos, cores):
    """ Função utilizada para gerar textos ao longo do jogo """
    text_surface = font.render("{}".format(variavel), True, cores)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (pos[0],  pos[1])
    window.blit(text_surface, (pos[0],  pos[1]))
    return 0

def tecla_pressionada(player1, player2,player1_esc,player2_esc):
    """ Função que interpreta todos os eventos e gera resultados para cada um deles"""
    for event in pygame.event.get():
        # Verifica se apertou alguma tecla.
        if event.type == pygame.KEYDOWN:
# ----------Movimentação do player 2 (Setinhas):
            if event.key == pygame.K_LEFT:
                player2.orientacao = 0
                if player2_esc != 2 or (player2_esc == 2 and player2.life >= 100):
                    player2.speedx += -8
                elif (player2_esc == 2 or player2_esc == 6) and player2.life < 100:
                    player2.speedx += -12
            
            if event.key == pygame.K_RIGHT:
                player2.orientacao = 1
                if player2_esc != 2 or (player2_esc == 2 and player2.life >= 100):
                    player2.speedx += 8
                elif (player2_esc == 2 or player2_esc == 6) and player2.life < 100:
                    player2.speedx += 12

            if event.key == pygame.K_UP:
                player2.jump()

# ----------Movimentação do player 1 (W,A,D):
            if event.key == pygame.K_a:
                player1.orientacao = 0
                if player1_esc != 2 or (player1_esc == 2 and player1.life >= 100):
                    player1.speedx += -8
                elif (player1_esc == 2 or player1_esc == 6) and player1.life < 100:
                    player1.speedx += -12
            
            if event.key == pygame.K_d:
                player1.orientacao = 1
                if player1_esc != 2 or (player1_esc == 2 and player1.life >= 100):
                    player1.speedx += 8
                elif (player1_esc == 2 or player1_esc == 6) and player1.life < 100:
                    player1.speedx += 12


            if event.key==pygame.K_w:
                player1.jump()

# ----------Tiros (Q, L):            
            if event.key==pygame.K_c and player1.life > 0 and player1.segundostiro == 0:
                if player1_esc == 3:
                    humberto_shoot_sound.stop()
                    humberto_shoot_sound.play()
                player1.shoot()
                player1.segundostiro = 64
            if event.key==pygame.K_l and player2.life > 0 and player2.segundostiro == 0:
                if player2_esc == 3:
                    humberto_shoot_sound.stop()
                    humberto_shoot_sound.play()
                player2.shoot()
                player2.segundostiro = 64

# ----------Sprite do soco (E, <):
            if event.key == pygame.K_v and player1.segundossoco == 0:
                if player1.orientacao == 0:
                    player1.rect.x -= 30
                elif player1.orientacao == 1:
                    player1.rect.x += 30
                if player1_esc == 1:
                    dio_soco_sound.stop()
                    dio_soco_sound.play()
                if player1_esc == 4:
                    honda_soco_sound.stop()
                    honda_soco_sound.play()
                if player1_esc == 5:
                    yoshi_soco_sound.stop()
                    yoshi_soco_sound.play()
                player1.punch()
                player1.segundossoco = 30
            if event.key == pygame.K_COMMA and player2.segundossoco == 0:
                if player2.orientacao == 0:
                    player2.rect.x -= 30
                elif player2.orientacao == 1:
                    player2.rect.x += 30
                if player2_esc == 1:
                    dio_soco_sound.stop()
                    dio_soco_sound.play()
                if player2_esc == 4:
                    honda_soco_sound.stop()
                    honda_soco_sound.play()
                if player2_esc == 5:
                    yoshi_soco_sound.stop()
                    yoshi_soco_sound.play()
                player2.punch()
                player2.segundossoco = 30
            
            print(player1.speedx, " ", player2.speedx)
                
        # Verifica se soltou alguma tecla.
        if event.type == pygame.KEYUP:
            # Dependendo da tecla, altera a velocidade.

            # Player 1
            if event.key == pygame.K_a:
                if player1_esc != 2 or (player1_esc == 2 and player1.life >= 100):
                    player1.speedx += +8
                elif (player1_esc == 2 or player1_esc == 6) and player1.life < 100:
                    player1.speedx += +12
            
            if event.key == pygame.K_d:
                if player1_esc != 2 or (player1_esc == 2 and player1.life >= 100):
                    player1.speedx += -8
                elif (player1_esc == 2 or player1_esc == 6) and player1.life < 100:
                    player1.speedx += -12

            # Player 2
            if event.key == pygame.K_LEFT:
                if player2_esc != 2 or (player2_esc == 2 and player2.life >= 100):
                    player2.speedx += 8
                elif (player2_esc == 2 or player2_esc == 6) and player2.life < 100:
                    player2.speedx = 0
            
            if event.key == pygame.K_RIGHT:
                if player2_esc != 2 or (player2_esc == 2 and player2.life >= 100):
                    player2.speedx += -8
                elif (player2_esc == 2 or player2_esc == 6) and player2.life < 100:
                    player2.speedx = 0

            if event.key == pygame.K_UP:
                player2.jump()
            
            print(player1.speedx, " ", player2.speedx)
            
        # Verifica se o jogo foi fechado
        if event.type == pygame.QUIT:
            pygame.quit()
    return True

def encostou(player1, player2, ph1, ph2):
    """ Função que verifica se o soco de um personagem atingiu o outro e causa o dano com condicionais, como personagem específico tirar mais dano
        
        ph1 e ph2 são as variáveis que armazenam a escolha dos jogadores, assim o código abaixo sabe como reagir para cada personagem com
        característica especial """
    if player2.image in player2.punch_img or player2.image in player2.goldpunch_img:
        if player2.umsoco == 1:
            player1.life -= player2.damage
            player2.umsoco = 0
            if player2.image in player2.goldpunch_img and (ph2 == 1 or ph2 == 6):
                player1.life -= 5
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
            if player1.image in player1.goldpunch_img and (ph1 == 1 or ph1 == 6):
                player2.life -= 5
    if player2.rect.centerx >= player1.rect.centerx:
        player2.rect.x += 30
    if player2.rect.centerx < player1.rect.centerx:
        player2.rect.x -= 30
    if player2.life<=0:
        player2.kill()
    return 0

def barrasdevida(player2,player1,barradevidaplayer1,barradevidaplayer2,barradevidacomvitorias_img):
    """ Função que atualiza as barras de vida dos jogadores conforme eles perdem vida """
    barradevidaplayer1.playerlife = player1.life
    barradevidaplayer2.playerlife = player2.life
    if player1.life > 0 or player2.life > 0:
        barradevidaplayer1.compbarraverd = 300*((barradevidaplayer1.playerlife-100)/100)
        barradevidaplayer2.compbarraverd = 300*((barradevidaplayer2.playerlife-100)/100)
        barradevidaplayer1.compbarraverm = 300*(barradevidaplayer1.playerlife/100)
        barradevidaplayer2.compbarraverm = 300*(barradevidaplayer2.playerlife/100)
    if barradevidaplayer1.playerlife > 100:
        barradevidaplayer1.barraverde_img = pygame.transform.scale(barradevidaplayer1.barraverde_img, (barradevidaplayer1.compbarraverd, 40))
    elif barradevidaplayer1.playerlife <= 100 and barradevidaplayer1.playerlife > 5:
        barradevidaplayer1.barravermelha_img = pygame.transform.scale(barradevidaplayer1.barravermelha_img, (barradevidaplayer1.compbarraverm, 40))
    if barradevidaplayer2.playerlife > 100:
        barradevidaplayer2.barraverde_img = pygame.transform.scale(barradevidaplayer2.barraverde_img, (barradevidaplayer2.compbarraverd, 40))
    elif barradevidaplayer2.playerlife <= 100 and barradevidaplayer2.playerlife > 5:
        barradevidaplayer2.barravermelha_img = pygame.transform.scale(barradevidaplayer2.barravermelha_img, (barradevidaplayer2.compbarraverm, 40))
    window.blit(barradevidaplayer1.barravermelha_img, (19, 10))
    if player1.life > 100:
        window.blit(barradevidaplayer1.barraverde_img, (19, 10))
    window.blit(barradevidaplayer2.barravermelha_img, (484, 10))
    if player2.life > 100:
        window.blit(barradevidaplayer2.barraverde_img, (484, 10))
    if player1.life <= 0:
        barradevidaplayer1.compbarraverd = 0
        barradevidaplayer1.compbarraverm = 0
        barradevidacomvitorias_img = pygame.transform.scale(barradevidacomvitorias_img, (311, 90))
        window.blit(barradevidacomvitorias_img, (15, 5))
    elif player2.life <= 0:
        barradevidaplayer2.compbarraverd = 0
        barradevidaplayer2.compbarraverm = 0
        barradevidacomvitorias_img = pygame.transform.scale(barradevidacomvitorias_img, (311, 90))
        window.blit(barradevidacomvitorias_img, (480, 5))
    return 0

def verificaplayer1ganhou(player2,podeacabar,player1vitorias,timer2,segundos3):
    """ Função que verifica se o player 1 ganhou e gera resultados """
    if player2.life <= 0 and podeacabar == False:
        texto(font2, "Player 1 wins" , [145, HEIGHT/2], (255,255,255))
        podeacabar = True
        timer2 = 0
    elif player2.life <= 0 and podeacabar == True:
        texto(font2, "Player 1 wins" , [145, HEIGHT/2], (255,255,255))
        segundos3 -= 1
        if segundos3==1:
            if timer2 <= 5:
                timer2 += 1
                print(timer2)
            segundos3 = 64
    if timer2 >= 5:
        player1vitorias += 1
        print(player1vitorias)
        return ['acabou',player1vitorias]
    return [segundos3, timer2, podeacabar]

def verificaplayer2ganhou(player1,podeacabar,player2vitorias,timer2,segundos3):
    """ Função que verifica se o player 2 ganhou e gera resultados """
    if player1.life <= 0 and podeacabar == False:
        texto(font2, "Player 2 wins" , [145, HEIGHT/2], (255,255,255))
        podeacabar = True
        timer2 = 0
    elif player1.life <= 0 and podeacabar == True:
        texto(font2, "Player 2 wins" , [145, HEIGHT/2], (255,255,255))
        segundos3 -= 1
        if segundos3==1:
            if timer2 <= 5:
                timer2 += 1
                print(timer2)
            segundos3 = 64
    if timer2 >= 5:
        player2vitorias += 1
        print(player2vitorias)
        return ['acabou',player2vitorias]
    return [segundos3, timer2, podeacabar]

def temporizador(segundos,tempo,podecomecar,player1,player2):
    """ Função que converte os ticks em segundos e serve como cooldown para algumas features """
    segundos -= 1
    tempo = tempo
    podecomecar = podecomecar
    player1 = player1
    player2 = player2
    if segundos <= 0 and podecomecar == True and player1.life > 0 and player2.life > 0:
        tempo -= 1
        segundos = 64
        player1.umsoco = 1
        player2.umsoco = 1
    return [segundos,tempo,player1.umsoco,player2.umsoco]