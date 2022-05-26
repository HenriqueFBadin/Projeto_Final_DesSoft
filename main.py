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

# ----- Inicia estruturas de dados
game = True

# ----- Agrupando as sprites
all_sprites = pygame.sprite.Group()
all_powers=pygame.sprite.Group()
sprite_p1= pygame.sprite.Group()
sprite_p2= pygame.sprite.Group()
sprite_power1=pygame.sprite.Group()
sprite_power2=pygame.sprite.Group()
sprite_punch=pygame.sprite.Group()

# ----- Definindo os Players 

player1 = Player(1, [pl_wolf_img, pr_wolf_img], [pl_wolf2_img, pr_wolf2_img], all_sprites, all_powers, sprite_power1, power_img, sprite_punch, [sl_wolf_img, sr_wolf_img], [sl_humb2_img, sl_humb2_img], [al_humb_img, al_humb_img], [al_humb_img, al_humb_img])
player2 = Player(0, [pl_humb_img, pr_humb_img], [pl_humb2_img, pl_humb2_img], all_sprites, all_powers, sprite_power2, power2_img, sprite_punch, [sl_humb_img, sl_humb_img], [sl_humb2_img, sl_humb2_img], [al_humb_img, al_humb_img], [al_humb_img, al_humb_img])
all_sprites.add(player1)
all_sprites.add(player2)
sprite_p1.add(player1)
sprite_p2.add(player2)

# ----- Colisões dos Players

# ===== Loop principal =====
while game:
    #Define tick rate
    clock.tick(tick_rate)
    # ----- Trata evento
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False
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
            if event.key==pygame.K_q and player1.life > 0:
                player1.shoot()
            if event.key==pygame.K_l and player2.life > 0:
                player2.shoot()

# ----------Sprite do soco (E, <):
            if event.key == pygame.K_e:
                player1.punch()
            if event.key == pygame.K_COMMA:
                player2.punch()
                
        
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

    # ----- Atualiza estado do jogo
    # Atualizando a situação dos players
    all_sprites.update()

    # ----- Gera saídas
    window.fill((255, 255, 255))  # Preenche com a cor branca
    window.blit(background_img,(0,0))
    # Desenhando os players
    all_sprites.draw(window)

    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador
    
    # ----- Base para colisões dos Players

    hit_power1=pygame.sprite.groupcollide(sprite_power1, sprite_p2, deathpower1, death2, pygame.sprite.collide_mask)
    if hit_power1:
        player2.life-=(player1.damage-5)
        deathpower1=True
        if player2.life<=0:
            death2=True
            
    hit_power2=pygame.sprite.groupcollide(sprite_power2, sprite_p1, deathpower2, death1, pygame.sprite.collide_mask)
    if hit_power2:
        player1.life-=(player2.damage-5)
        deathpower2=True
        if player1.life<=0:
            death1=True
    

    hit1=pygame.sprite.spritecollide(player2, sprite_p1, death1)
    hit2=pygame.sprite.spritecollide(player1, sprite_p2, death2, pygame.sprite.collide_mask)

########################TOMAR CUIDADO! AS IMAGENS N SÃO VARIAVEIS, MUDAR NA HORA QUE TIVER + DE 2 PERSONAGENS PARA N DAR CONFLITO#####################  
    if hit1:
        if player1.image == sr_Teste_img or player1.image==sl_humb2_img:
            player2.life -= player1.damage
        if player2.rect.centerx >= player1.rect.centerx:
            player2.rect.x += 30
        if player2.rect.centerx < player1.rect.centerx:
            player2.rect.x -= 30
        hit1=[]
        if player2.life<=0:            
            death2=True

    if hit2:
        if player2.image == sl_humb_img or player2.image==sl_humb2_img:
            player1.life -= player2.damage
            player2.rect.centerx += 50
        if player1.rect.centerx >= player2.rect.centerx:
            player1.rect.x += 30
        if player1.rect.centerx < player2.rect.centerx:
            player1.rect.x -= 30
        hit2=[]
        if player1.life<=0:            
            death1=True

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados