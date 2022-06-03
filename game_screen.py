print("Criadores do projeto: Eduardo Selber Castanho, Henrique Fazzio Badin, Henrique Rocha Bomfim")
# ===== Inicialização =====
# ----- Importa e inicia pacotes
from sre_parse import State
from time import sleep, time
#from turtle import delay
import pygame
from assets import *
from character_selection import INIT
from classes import *
from funcoes import *
state=0
# ===== Loop principal =====
pygame.mixer.music.play(loops=-1)
def game_screen(window,player1_esc,player2_esc):
    rodada = 1
    p1h=player1_esc
    p2h=player2_esc
    def rodada_do_jogo(p1h,p2h):
        all_sprites = pygame.sprite.Group()
        all_powers=pygame.sprite.Group()
        sprite_p1= pygame.sprite.Group()
        sprite_p2= pygame.sprite.Group()
        sprite_power1=pygame.sprite.Group()
        sprite_power2=pygame.sprite.Group()
        sprite_punch=pygame.sprite.Group()

        # ----- Definindo os Players 
        player1 = Player(1, all_sprites, all_powers, sprite_power1, sprite_punch, imagens[p1h][0], imagens[p1h][1], imagens[p1h][2], imagens[p1h][3], imagens[p1h][4], imagens[p1h][5], imagens[p1h][6], imagens[p1h][7], imagens[p1h][8])
        player2 = Player(0, all_sprites, all_powers, sprite_power2, sprite_punch, imagens[p2h][0], imagens[p2h][1], imagens[p2h][2], imagens[p2h][3], imagens[p2h][4], imagens[p2h][5], imagens[p2h][6], imagens[p2h][7], imagens[p2h][8])
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
        segundos3=64
        podeacabar = False
        Player1life = 'P1'
        Player2life = 'P2'
        barraverde_img = pygame.image.load('Imagem/barraverde.png').convert_alpha()
        barravermelha_img = pygame.image.load('Imagem/barravermelha.png').convert_alpha()
        barradevida1_img = pygame.image.load('Imagem/barradevida.png').convert_alpha()
        barraverde_img = pygame.image.load('Imagem/barraverde.png').convert_alpha()
        barravermelha_img = pygame.image.load('Imagem/barravermelha.png').convert_alpha()
        barradevida2_img = pygame.image.load('Imagem/barradevida.png').convert_alpha()
        barradevidaplayer1 = BarraHp(player1.life,1,barravermelha_img,barraverde_img)
        barradevidaplayer2 = BarraHp(player2.life,2,barravermelha_img,barraverde_img)

        timer = 0
        timer2=0
        while game:
            # Define tick rate
            clock.tick(tick_rate)

            # Tecla é pressionada
            if podecomecar == True:
                tecla_pressionada(player1, player2,player1_esc,player2_esc)
            
            # Verifica os disparos e causa o dano
            hit_power1=pygame.sprite.groupcollide(sprite_power1, sprite_p2, deathpower1, death2, pygame.sprite.collide_mask)
            hit_power2=pygame.sprite.groupcollide(sprite_power2, sprite_p1, deathpower2, death1, pygame.sprite.collide_mask)
            if hit_power1:
                player2.life-=(player1.damage-5)
                deathpower1=True
            if hit_power2:
                player1.life-=(player2.damage-5)
                deathpower2=True

            # Verifica os socos e causa os danos
            hit = pygame.sprite.spritecollide(player2, sprite_p1, death1, pygame.sprite.collide_mask)
            if hit:
                encostou(player1, player2)
                hit = []

            #Timer
            segundos -= 1
            if segundos <= 0 and podecomecar == True and player1.life > 0 and player2.life > 0:
                tempo -= 1
                segundos = 64
                player1.umsoco = 1
                player2.umsoco = 1
            if tempo <= 0:
                return 1

            # Atualizando a situação dos players
            all_sprites.update()

            # ----- Gera saídas
            window.fill((255, 255, 255))  # Preenche com a cor branca
            window.blit(background4_img,(0,0))
            barradevida1_img = pygame.transform.scale(barradevida1_img, (310, 60))
            barradevida2_img = pygame.transform.scale(barradevida2_img, (310, 60))
            window.blit(barradevida1_img, (15, 5))
            window.blit(barradevida2_img, (480, 5))

            # Barra de vida e finalização
            barrasdevidaefinalização(player2,player1,barradevidaplayer1,barradevidaplayer2)
            
            texto(font, tempo, [WIDTH/2 -10,10], (0,0,0))
            texto(font, Player1life , [25, 15], (0,0,0))
            texto(font, Player2life , [490, 15], (0,0,0))
            if player1.life <= 0 and podeacabar == False:
                texto(font2, "Player 2 wins" , [145, HEIGHT/2], (255,255,255))
                podeacabar = True
                timer2 = 0
            if player1.life <= 0 and podeacabar == True:
                texto(font2, "Player 2 wins" , [145, HEIGHT/2], (255,255,255))
                segundos3 -= 1
                if segundos3==1:
                    if timer2 <= 5:
                        timer2 += 1
                    segundos3 = 64
                if timer2 >= 5:
                    return 0      
                
            if player2.life <= 0 and podeacabar == False:
                texto(font2, "Player 1 wins" , [145, HEIGHT/2], (255,255,255))
                podeacabar = True
                timer2 = 0
            if player2.life <= 0 and podeacabar == True:
                texto(font2, "Player 1 wins" , [145, HEIGHT/2], (255,255,255))
                segundos3 -= 1
                if segundos3==1:
                    if timer2 <= 5:
                        timer2 += 1
                    segundos3 = 64
                if timer2 >= 5:
                    return 0       

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
    rodada_do_jogo(p1h,p2h)
    #delay(3000)
    return INIT
    
