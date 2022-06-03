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
state = 0
# ===== Loop principal =====
pygame.mixer.music.play(loops=-1)
def game_screen(window,player1_esc,player2_esc):
    p1h=player1_esc
    p2h=player2_esc
    player1vitorias = 0
    player2vitorias = 0
    resultadorodada = []
    rodada = 0
    # Obs: A ordem das sprites foi feita de acordo com qual camada queremos colocá-las, para evitar sobreposições indesejadas
    while rodada < 4:
        rodada += 1
        print(rodada)
        def rodada_do_jogo(p1h,p2h,rodada,player1vitorias,player2vitorias):
            # Agrupando sprites
            all_sprites = pygame.sprite.Group()
            all_powers=pygame.sprite.Group()
            sprite_p1= pygame.sprite.Group()
            sprite_p2= pygame.sprite.Group()
            sprite_power1=pygame.sprite.Group()
            sprite_power2=pygame.sprite.Group()
            sprite_punch=pygame.sprite.Group()

            # Criando os players e suas barras de vida
            player1 = Player(1, all_sprites, all_powers, sprite_power1, sprite_punch, imagens[p1h][0], imagens[p1h][1], imagens[p1h][2], imagens[p1h][3], imagens[p1h][4], imagens[p1h][5], imagens[p1h][6], imagens[p1h][7], imagens[p1h][8])
            player2 = Player(0, all_sprites, all_powers, sprite_power2, sprite_punch, imagens[p2h][0], imagens[p2h][1], imagens[p2h][2], imagens[p2h][3], imagens[p2h][4], imagens[p2h][5], imagens[p2h][6], imagens[p2h][7], imagens[p2h][8])
            barradevidaplayer1 = BarraHp(player1.life,1,barravermelha_img,barraverde_img)
            barradevidaplayer2 = BarraHp(player2.life,2,barravermelha_img,barraverde_img)

            # Adicionando os players aos seus devidos grupos
            all_sprites.add(player1)
            all_sprites.add(player2)
            sprite_p1.add(player1)
            sprite_p2.add(player2)

            # Definindo variáveis
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
            player1ganhou = []
            player2ganhou = []
            resultado_temporizador = []
            Player1life = 'P1'
            Player2life = 'P2'
            timer = 0
            timer2 = 0

            # Loop do jogo
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

                # Timer
                temporizador(segundos,tempo,podecomecar,player1,player2)
                resultado_temporizador = temporizador(segundos,tempo,podecomecar,player1,player2)
                segundos = resultado_temporizador[0]
                tempo = resultado_temporizador[1]
                player1.umsoco = resultado_temporizador[2]
                player2.umsoco = resultado_temporizador[3]
                if tempo <= 0:
                    return 1
                
                # Atualizando a situação dos players
                all_sprites.update()

                # Exibe o background e os fundos das barras de vida
                window.blit(background4_img,(0,0))
                window.blit(barradevida_img, (15, 5))
                window.blit(barradevida_img, (480, 5))

                # Barras de vida e finalização
                barrasdevida(player2,player1,barradevidaplayer1,barradevidaplayer2,barradevida1_img,barradevida2_img)
                verificaplayer1ganhou(player2,podeacabar,player1vitorias,timer2,segundos3)
                verificaplayer2ganhou(player1,podeacabar,player2vitorias,timer2,segundos3)

                player1ganhou = verificaplayer1ganhou(player2,podeacabar,player1vitorias,timer2,segundos3)
                if player1ganhou[0] != 'acabou':
                    segundos3 = player1ganhou[0]
                    timer2 = player1ganhou[1]
                    podeacabar = player1ganhou[2]
                else:
                    player1vitorias = player1ganhou[1]
                    player2vitorias = player2vitorias
                    return [player1vitorias,player2vitorias]

                player2ganhou = verificaplayer2ganhou(player1,podeacabar,player2vitorias,timer2,segundos3)
                if player2ganhou[0] != 'acabou':
                    segundos3 = player2ganhou[0]
                    timer2 = player2ganhou[1]
                    podeacabar = player2ganhou[2]
                else:
                    player1vitorias = player1vitorias
                    player2vitorias = player2ganhou[1]
                    return [player1vitorias,player2vitorias]
                
                #Imprime o tempo e os textos "P1" e "P2"
                texto(font, tempo, [WIDTH/2 -10,10], (0,0,0))
                texto(font, Player1life , [25, 15], (0,0,0))
                texto(font, Player2life , [490, 15], (0,0,0))
                
                # Faz a contagem inicial para os jogadores poderem lutar
                valores = [3,2,1,0,'Go!',' ']
                segundos2 -= 1
                if timer == 0:
                    text_surface2 = font2.render("{}".format(valores[timer]), True, (255, 255, 0))
                if segundos2 <= 0 and timer <= 5:
                    if timer < 6:
                        text_surface2 = font2.render("{}".format(valores[timer]), True, (255, 255, 0))
                        text_rect = text_surface2.get_rect()
                        text_rect.midtop = (400,  400)
                        timer += 1
                    segundos2 = 64
                if timer != 5 and podecomecar == False:
                    texto(font2, "Round {}".format(rodada) , [WIDTH/2 - 120,  HEIGHT/2 - 225], (255,255,255))
                if timer == 5:
                    podecomecar = True
                window.blit(text_surface2, (WIDTH/2 - 10,  HEIGHT/2))

                # Desenhando todos os sprites
                all_sprites.draw(window)

                # ----- Atualiza estado do jogo
                pygame.display.update()  # Mostra o novo frame para o jogador

            # ===== Finalização =====
            pygame.quit()  # Função do PyGame que finaliza os recursos utilizados
        #Inicia a função da rodada do jogo
        resultadorodada = rodada_do_jogo(p1h,p2h,rodada,player1vitorias,player2vitorias)
        player1vitorias = resultadorodada[0]
        player2vitorias = resultadorodada[1]
        print(player1vitorias,player2vitorias)
        if player1vitorias >= 2 or player2vitorias >= 2:
            break
    return 5