print("Criadores do projeto: Eduardo Selber Castanho, Henrique Fazzio Badin, Henrique Rocha Bomfim")
# ===== Inicialização =====
# ----- Importa e inicia pacotes
from time import time
import pygame
from classes import *
from assets import *

pygame.init()

# ----- Gera tela principal
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Mortal Insper!')

# ----- Agrupando as sprites
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

# ----- Colisões dos Players

# ===== Loop principal =====
while game:
    # Define tick rate
    clock.tick(tick_rate)

    # Tecla é pressionada
    tecla_pressionada(player1, player2, segundos)
    
    # Verifica os disparos e causa o dano
    hit_power1=pygame.sprite.groupcollide(sprite_power1, sprite_p2, deathpower1, death2, pygame.sprite.collide_mask)
    hit_power2=pygame.sprite.groupcollide(sprite_power2, sprite_p1, deathpower2, death1, pygame.sprite.collide_mask)
    if hit_power1:
        player2.life-=(player1.damage-5)
        deathpower1=True
        if player2.life<=0:
            death2=True
    if hit_power2:
        player1.life-=(player2.damage-5)
        deathpower2=True
        if player1.life<=0:
            death1=True

    # Verifica os socos e causa os danos
    hit = pygame.sprite.spritecollide(player2, sprite_p1, death1, pygame.sprite.collide_mask)
    if hit:
        encostou(player1, player2)
        hit = []
    verificamorreu(player1, player2)

    #Timer
    segundos -= 1
    if segundos <= 0:
        tempo -= 1
        segundos = 64
    if tempo <= 0:
        pygame.quit()

    # Atualizando a situação dos players
    all_sprites.update()

    # ----- Gera saídas
    window.fill((255, 255, 255))  # Preenche com a cor branca
    window.blit(background4_img,(0,0))
    window.blit(barradefundo_img, (10, 5))
    window.blit(barradefundotempo_img, (WIDTH/2 - 20, 10))
    window.blit(barradefundo_img, (500, 5))
    texto(font, tempo, [WIDTH/2,10])
    Player1life = 'Player1 Life: {}'.format(player1.life)
    Player2life = 'Player2 Life: {}'.format(player2.life)

    texto(font, Player1life , [15, 10])
    texto(font, Player2life , [510, 10])
    # Desenhando os players
    all_sprites.draw(window)

    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados