import pygame

pygame.init()
# ----- Gera tela principal
window = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Mortal Insper!')

#VARIÁVEIS:
P1_WIDTH=150
P1_HEIGHT=150
WIDTH=800
HEIGHT=600
death1=False
death2=False
deathpower1=False
deathpower2=False

#CONTROLE DE FPS
clock = pygame.time.Clock()
tick_rate = 64


#IMAGENS:
pl_humb_img=pygame.image.load('Imagem/HUmberto-ryu0.png').convert_alpha()
pr_humb_img=pygame.image.load('Imagem/Humbertodireita.png').convert_alpha()
sr_Teste_img = pygame.image.load('Imagem/Quadrado_Teste_socando.png').convert_alpha()
sl_humb_img = pygame.image.load('Imagem/hu soco.png').convert_alpha()
sr_humb_img = pygame.image.load('Imagem/hu socoesq.png').convert_alpha()
al_humb_img = pygame.image.load('Imagem/humberto haduken.png').convert_alpha()
jl_humb_img = pygame.image.load('Imagem/humberto pulando esquerda.png').convert_alpha()
jr_humb_img = pygame.image.load('Imagem/humberto pulando direita.png').convert_alpha()
pl_humb2_img=pygame.image.load('Imagem/hugold.png').convert_alpha()
pr_humb2_img=pygame.image.load('Imagem/hugolddireita.png').convert_alpha()
pr_wolf2_img = pygame.image.load('Imagem/werewolf_golden.png').convert_alpha() 
pl_wolf2_img = pygame.image.load('Imagem/werewolf_golden_parado_esquerda.png').convert_alpha()
sl_humb2_img=pygame.image.load('Imagem/hugold soco.png').convert_alpha()
pr_wolf_img = pygame.image.load('Imagem/werewolf.png').convert_alpha()
pl_wolf_img = pygame.image.load('Imagem/werewolf_parado_esquerda.png').convert_alpha()
sr_wolf_img = pygame.image.load('Imagem/werewolf soco direita final.png').convert_alpha()
sl_wolf_img = pygame.image.load('Imagem/werewolf soco esquerda final.png').convert_alpha()
power_img=pygame.image.load('Imagem/haduken.png').convert_alpha()
power2_img=pygame.image.load('Imagem/hadukenfogo.png').convert_alpha()
background_img = pygame.image.load('Imagem/cenário.jpg').convert_alpha()
background2_img = pygame.image.load('Imagem/Background2.png').convert_alpha()
background3_img = pygame.image.load('Imagem/Background3.png').convert_alpha()
background4_img = pygame.image.load('Imagem/Background4.png').convert_alpha()
pr_dio_img=pygame.image.load('Imagem/DIO_Parado_Direita.png').convert_alpha() 
pl_dio_img=pygame.image.load('Imagem/DIO_Parado_Esquerda.png').convert_alpha() 
sr_dio_img=pygame.image.load('Imagem/DIO_Socando_Direita.png').convert_alpha() 
sl_dio_img=pygame.image.load('Imagem/DIO_Socando_Esquerda.png').convert_alpha() 
ar_dio_img=pygame.image.load('Imagem/DIO_Atirando_Direita.png').convert_alpha() 
al_dio_img=pygame.image.load('Imagem/DIO_Atirando_Esquerda.png').convert_alpha() 
jl_dio_img=pygame.image.load('Imagem/DIO_pulando_esquerda.png').convert_alpha() 
jr_dio_img=pygame.image.load('Imagem/DIO_pulando_direita.png').convert_alpha() 
pl_humb_img=pygame.transform.scale(pl_humb_img, (P1_WIDTH, P1_HEIGHT+30))
pr_humb_img=pygame.transform.scale(pr_humb_img, (P1_WIDTH, P1_HEIGHT+30))
pr_wolf_img=pygame.transform.scale(pr_wolf_img, (P1_WIDTH, P1_HEIGHT+30))
pl_wolf_img=pygame.transform.scale(pl_wolf_img, (P1_WIDTH, P1_HEIGHT+30))
pr_wolf2_img=pygame.transform.scale(pr_wolf2_img, (P1_WIDTH, P1_HEIGHT+30))
pl_wolf2_img=pygame.transform.scale(pl_wolf2_img, (P1_WIDTH, P1_HEIGHT+30))
sr_wolf_img=pygame.transform.scale(sr_wolf_img, (P1_WIDTH+30, P1_HEIGHT+30))
sl_wolf_img=pygame.transform.scale(sl_wolf_img, (P1_WIDTH+30, P1_HEIGHT+30))
sr_Teste_img=pygame.transform.scale(sr_Teste_img, (200+30, P1_HEIGHT))
sl_humb_img=pygame.transform.scale(sl_humb_img, (200+30, P1_HEIGHT+30))
sr_humb_img=pygame.transform.scale(sr_humb_img, (200+30, P1_HEIGHT+30))
al_humb_img=pygame.transform.scale(al_humb_img, (200+30, P1_HEIGHT+30))
jl_humb_img=pygame.transform.scale(jl_humb_img, (180, P1_HEIGHT+30))
jr_humb_img=pygame.transform.scale(jr_humb_img, (180, P1_HEIGHT+30))
pl_humb2_img=pygame.transform.scale(pl_humb2_img, (150, P1_HEIGHT+30))
pr_humb2_img=pygame.transform.scale(pr_humb2_img, (150, P1_HEIGHT+30))
sl_humb2_img=pygame.transform.scale(sl_humb2_img, (180+30, P1_HEIGHT+30))
pr_dio_img=pygame.transform.scale(pr_dio_img, (180, P1_HEIGHT+30))
pl_dio_img=pygame.transform.scale(pl_dio_img, (180, P1_HEIGHT+30))
sr_dio_img=pygame.transform.scale(sr_dio_img, (180, P1_HEIGHT+30))
sl_dio_img=pygame.transform.scale(sl_dio_img, (180, P1_HEIGHT+30))
ar_dio_img=pygame.transform.scale(ar_dio_img, (180, P1_HEIGHT+30))
al_dio_img=pygame.transform.scale(al_dio_img, (180, P1_HEIGHT+30))
jl_dio_img=pygame.transform.scale(jl_dio_img, (200, P1_HEIGHT+30))
jr_dio_img=pygame.transform.scale(jr_dio_img, (200, P1_HEIGHT+30))
power_img=pygame.transform.scale(power_img,(80,80))
power2_img=pygame.transform.scale(power2_img,(80,80))
background_img=pygame.transform.scale(background_img, (WIDTH, HEIGHT))
background2_img=pygame.transform.scale(background2_img, (WIDTH, HEIGHT))
background3_img=pygame.transform.scale(background3_img, (WIDTH, HEIGHT))
background4_img=pygame.transform.scale(background4_img, (WIDTH+30, HEIGHT))