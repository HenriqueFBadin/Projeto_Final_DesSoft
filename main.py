print("Criadores do projeto: Eduardo Selber Castanho, Henrique Fazzio Badin, Henrique Rocha Bomfim")
# ===== Inicialização =====
# ----- Importa e inicia pacotes
from time import time
import pygame
from classes import *
import time
P1_WIDTH=150
P1_HEIGHT=150
WIDTH=800
HEIGHT=600
death1=False
death2=False
deathpower1=False
deathpower2=False
contador_soco_1 = 10
contador_soco_2 = 10

pygame.init()
# ----- Gera tela principal
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Mortal Insper!')

# ----- Inicia estruturas de dados
game = True
p1_img=pygame.image.load('Imagem/Quadrado_Teste.png').convert_alpha()
p2_img=pygame.image.load('Imagem/Quadrado_Teste_2.png').convert_alpha()
p1socando_img = pygame.image.load('Imagem/Quadrado_Teste_socando.png').convert_alpha()
p2socando_img = pygame.image.load('Imagem/Quadrado_Teste_2_socando.png').convert_alpha()
p1_img=pygame.transform.scale(p1_img, (P1_WIDTH, P1_HEIGHT))
p2_img=pygame.transform.scale(p2_img, (P1_WIDTH, P1_HEIGHT))
p1socando_img=pygame.transform.scale(p1socando_img, (200, P1_HEIGHT))
p2socando_img=pygame.transform.scale(p2socando_img, (200, P1_HEIGHT))
power_img=pygame.image.load('Imagem/haduken.png').convert_alpha()
power_img=pygame.transform.scale(power_img,(80,80))
power2_img=pygame.image.load('Imagem/hadukenfogo.png').convert_alpha()
power2_img=pygame.transform.scale(power2_img,(80,80))
background_img = pygame.image.load('Imagem/cenário.jpg').convert_alpha()
background_img=pygame.transform.scale(background_img, (WIDTH, HEIGHT))

# ----- Controle de FPS e Tick Rate
clock = pygame.time.Clock()
tick_rate = 64
#parametro pro jump:
isjump=False
jumpcount=1

# ----- Agrupando as sprites
all_sprites = pygame.sprite.Group()
all_powers=pygame.sprite.Group()
sprite_p1= pygame.sprite.Group()
sprite_p2= pygame.sprite.Group()
sprite_power1=pygame.sprite.Group()
sprite_power2=pygame.sprite.Group()

# ----- Definindo os Players
player1 = Player(p1_img,all_sprites,all_powers,power_img,power2_img)
player2 = Player(p2_img,all_sprites,all_powers,power_img,power2_img)
all_sprites.add(player1)
all_sprites.add(player2)
sprite_p1.add(player1)
sprite_p2.add(player2)

# ----- Colisões dos Players
#hit=pygame.sprite.spritecollide(player1, sprite_test, False)

# ===== Loop principal =====
while game:
    #Define tick rate
    clock.tick(tick_rate)
    #Cria jogadores
    # ----- Trata evento
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False
        # Verifica se apertou alguma tecla.
        if event.type == pygame.KEYDOWN:
            # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_LEFT:
                player2.speedx -= 8
            if event.key == pygame.K_RIGHT:
                player2.speedx += 8
            if event.key == pygame.K_a:
                player1.speedx -= 8
            if event.key == pygame.K_d:
                player1.speedx += 8
            if event.key==pygame.K_w:
                player1.jump()
            if event.key == pygame.K_UP:
                player2.jump()
            if event.key == pygame.K_UP:
                player2.speedy -= 8
            if event.key == pygame.K_w:
                player1.speedy -= 8
            if event.key==pygame.K_q:
                player1.shoot()
            if event.key==pygame.K_l:
                player2.shoot2()

            if event.key == pygame.K_e:
                player1.image = p1socando_img
            if event.key == pygame.K_COMMA:
                player2.image = p2socando_img
        
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
    if contador_soco_1 > 0 and player1.image == p1socando_img:
        contador_soco_1 -= 1
    elif contador_soco_1 <= 0:
        player1.image = p1_img
        contador_soco_1 = 10
    if contador_soco_2 > 0 and player2.image == p2socando_img:
        contador_soco_2 -= 1
    elif contador_soco_2 <= 0:
        player2.image = p2_img
        contador_soco_2 = 10
    #hits = pygame.sprite.spritecollideany(player1, player2, True)
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

    hit_power1=pygame.sprite.spritecollide(player2,all_powers,deathpower1)
    if hit_power1:
        player2.life-=10
        deathpower1=True
    hit_power2=pygame.sprite.spritecollide(player1,all_powers,deathpower2)
    if hit_power2:
        player1.life-=10
    

    hit1=pygame.sprite.spritecollide(player2, sprite_p1, death1)
    hit2=pygame.sprite.spritecollide(player1, sprite_p2, death2)

    if hit1 and player1.image == p1socando_img:
        player2.life-=10
        if player2.rect.centerx >= player1.rect.centerx:
            player2.rect.x += 30
        if player2.rect.centerx < player1.rect.centerx:
            player2.rect.x -= 30
        hit1=[]
        if player2.life<=0:            
            death2=True

    if hit2 and player2.image == p2socando_img:
        player1.life-=10
        if player1.rect.centerx >= player2.rect.centerx:
            player1.rect.x += 30
        if player1.rect.centerx < player2.rect.centerx:
            player1.rect.x -= 30
        hit2=[]
        if player1.life<=0:            
            death1=True

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados