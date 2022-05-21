print("Criadores do projeto: Eduardo Selber Castanho, Henrique Fazzio Badin, Henrique Rocha Bomfim")
# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
from classes import *


pygame.init()
# ----- Gera tela principal
WIDTH=1920
HEIGHT=1080
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Mortal Insper!')

# ----- Inicia estruturas de dados
game = True
p1_img=pygame.image.load('Imagem/Quadrado_Teste.png').convert_alpha()
p2_img=pygame.image.load('Imagem/Quadrado_Teste.png').convert_alpha()
p1_img=pygame.transform.scale(p1_img, (P1_WIDTH, P1_HEIGHT))
p2_img=pygame.transform.scale(p2_img, (P1_WIDTH, P1_HEIGHT))

# ----- Controle de FPS e Tick Rate
clock = pygame.time.Clock()
tick_rate = 64
#parametro pro jump:
isjump=False
jumpcount=10
Y_gravity=1
i=0
jump_height=200
Y_velocity=jump_height
# ----- Agrupando as sprites
all_sprites = pygame.sprite.Group()

# ----- Definindo os Players
player1 = p1(p1_img)
player2 = p2(p2_img)
all_sprites.add(player1)
all_sprites.add(player2)

# ===== Loop principal =====
while game:
    #Define tick rate
    clock.tick(tick_rate)
    #Cria jogadores
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False
        # Verifica se apertou alguma tecla.
        if event.type == pygame.KEYDOWN:
            # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_LEFT:
                player1.speedx -= 8
            if event.key == pygame.K_RIGHT:
                player1.speedx += 8
            if event.key == pygame.K_a:
                player2.speedx -= 8
            if event.key == pygame.K_d:
                player2.speedx += 8
            if not(isjump):
                if event.key==pygame.K_w:
                    isjump=True
            if isjump:
               if jumpcount>=-10:
                    if jumpcount>=0 and player2.speedy<jump_height:

                        player2.speedy-=2
                        jumpcount-=5
                    if jumpcount<0:
                        player2.speedy+=2
                        jumpcount-=5

            else:
                isjump=False
                jumpcount=10
                                       


            if event.key == pygame.K_UP:
                player1.speedy -= 8
        # Verifica se soltou alguma tecla.
        if event.type == pygame.KEYUP:
            # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_LEFT:
                player1.speedx += 8
            if event.key == pygame.K_RIGHT:
                player1.speedx -= 8
            if event.key == pygame.K_a:
                player2.speedx += 8
            if event.key == pygame.K_d:
                player2.speedx -= 8
            if event.key == pygame.K_w and player2.speedy>HEIGHT-P1_HEIGHT:
                player2.speedy += 8
            if event.key == pygame.K_UP:
                player1.speedy += 8
    # ----- Atualiza estado do jogo
    #hits = pygame.sprite.spritecollideany(player1, player2, True)
    # Atualizando a situação dos players
    all_sprites.update()

    # ----- Gera saídas
    window.fill((255, 255, 255))  # Preenche com a cor branca

    # Desenhando os players
    all_sprites.draw(window)

    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados

