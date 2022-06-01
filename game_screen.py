print("Criadores do projeto: Eduardo Selber Castanho, Henrique Fazzio Badin, Henrique Rocha Bomfim")
# ===== Inicialização =====
# ----- Importa e inicia pacotes
from time import time
import pygame
from assets import *
from classes import *
from funcoes import *

# ----- Colisões dos Players

# ===== Loop principal =====
def game_screen(window):
    all_sprites = pygame.sprite.Group()
    all_powers=pygame.sprite.Group()
    sprite_p1= pygame.sprite.Group()
    sprite_p2= pygame.sprite.Group()
    sprite_power1=pygame.sprite.Group()
    sprite_power2=pygame.sprite.Group()
    sprite_punch=pygame.sprite.Group()

    # ----- Definindo os Players 
    player1 = Player(1, all_sprites, all_powers, sprite_power1, sprite_punch, imagens[1][0], imagens[1][1], imagens[1][2], imagens[1][3], imagens[1][4], imagens[1][5], imagens[1][6], imagens[1][7], imagens[1][8])
    player2 = Player(0, all_sprites, all_powers, sprite_power2, sprite_punch, imagens[3][0], imagens[3][1], imagens[3][2], imagens[3][3], imagens[3][4], imagens[3][5], imagens[3][6], imagens[3][7], imagens[3][8])
    all_sprites.add(player1)
    all_sprites.add(player2)
    sprite_p1.add(player1)
    sprite_p2.add(player2)
    death1=False
    death2=False
    deathpower1=False
    deathpower2=False
    podecomecar=False
    tempo = 150
    segundos = 64
    segundos2 = 64
    Player1life = 'P1'
    Player2life = 'P2'
    barraverde1_img = pygame.image.load('Imagem/barraverde.png').convert_alpha()
    barravermelha1_img = pygame.image.load('Imagem/barravermelha.png').convert_alpha()
    barradevida1_img = pygame.image.load('Imagem/barradevida.png').convert_alpha()
    barraverde2_img = pygame.image.load('Imagem/barraverde.png').convert_alpha()
    barravermelha2_img = pygame.image.load('Imagem/barravermelha.png').convert_alpha()
    barradevida2_img = pygame.image.load('Imagem/barradevida.png').convert_alpha()

    timer = 0
    while game:
        # Define tick rate
        clock.tick(tick_rate)

        # Tecla é pressionada
        if podecomecar == True:
            tecla_pressionada(player1, player2, segundos)
        
        # Verifica os disparos e causa o dano
        hit_power1=pygame.sprite.groupcollide(sprite_power1, sprite_p2, deathpower1, death2, pygame.sprite.collide_mask)
        hit_power2=pygame.sprite.groupcollide(sprite_power2, sprite_p1, deathpower2, death1, pygame.sprite.collide_mask)
        if hit_power1:
            player2.life-=(player1.damage-5)
            if player1.compbarraverd > 0:
                player2.compbarraverd -= 13
            deathpower1=True
        if hit_power2:
            player1.life-=(player2.damage-5)
            if player1.compbarraverd > 0:
                player1.compbarraverd -= 13
            deathpower2=True

        # Verifica os socos e causa os danos
        hit = pygame.sprite.spritecollide(player2, sprite_p1, death1, pygame.sprite.collide_mask)
        if hit:
            encostou(player1, player2)
            hit = []
        verificamorreu(player1, player2)

        #Timer
        segundos -= 1
        if segundos <= 0 and podecomecar == True:
            tempo -= 1
            segundos = 64
            player1.umsoco = 1
            player2.umsoco = 1
        if tempo <= 0:
            pygame.quit()

        # Atualizando a situação dos players
        all_sprites.update()

        # ----- Gera saídas
        window.fill((255, 255, 255))  # Preenche com a cor branca
        window.blit(background4_img,(0,0))
        window.blit(barradefundotempo_img, (WIDTH/2 -14, 10))
        barradevida1_img = pygame.transform.scale(barradevida1_img, (310, 60))
        barradevida2_img = pygame.transform.scale(barradevida2_img, (310, 60))
        barravermelha1_img = pygame.transform.scale(barravermelha1_img, (player1.compbarraverm, 40))
        barraverde1_img = pygame.transform.scale(barraverde1_img, (player1.compbarraverd, 40))
        barravermelha2_img = pygame.transform.scale(barravermelha2_img, (player2.compbarraverm, 40))
        barraverde2_img = pygame.transform.scale(barraverde2_img, (player2.compbarraverd, 40))
        window.blit(barradevida1_img, (15, 5))
        window.blit(barradevida2_img, (480, 5))
        window.blit(barravermelha1_img, (19, 10))
        window.blit(barraverde1_img, (19, 10))
        window.blit(barravermelha2_img, (484, 10))
        window.blit(barraverde2_img, (484, 10))
        
        texto(font, tempo, [WIDTH/2 -10,10])
        texto(font, Player1life , [25, 15])
        texto(font, Player2life , [490, 15])

        valores = [3,2,1,0,'Go!',' ']
        segundos2 -= 1
        if timer == 0:
            text_surface2 = font2.render("{}".format(valores[timer]), True, (255, 0, 0))
        if segundos2 <= 0:
            if timer < 6:
                text_surface2 = font2.render("{}".format(valores[timer]), True, (255, 0, 0))
                text_rect = text_surface2.get_rect()
                text_rect.midtop = (400,  400)
                timer += 1
            segundos2 = 64
        if timer == 5:
            podecomecar = True
        window.blit(text_surface2, (WIDTH/2,  HEIGHT/2))

        # Desenhando os players
        all_sprites.draw(window)

        # ----- Atualiza estado do jogo
        pygame.display.update()  # Mostra o novo frame para o jogador

    # ===== Finalização =====
    pygame.quit()  # Função do PyGame que finaliza os recursos utilizados