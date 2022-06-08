import pygame

pygame.init()

import os
from os import path
# ----- Gera tela principal
window = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Mortal Insper!')

#VARIÁVEIS:
P1_WIDTH=150
P1_HEIGHT=150
WIDTH=800 #800
HEIGHT=600 #600
compbarraverd = 300
compbarraverm = 300
game = True
SND_DIR = path.join(path.dirname(__file__), 'Audios')

font = pygame.font.SysFont(None, 48)
font2 = pygame.font.SysFont(None, 100)
fontwins = pygame.font.SysFont(None, 30)

#CONTROLE DE FPS
clock = pygame.time.Clock()
tick_rate = 64


#IMAGENS:

pr_dio_img=pygame.image.load('Imagem/DIO_Parado_Direita.png').convert_alpha() 
pl_dio_img=pygame.image.load('Imagem/DIO_Parado_Esquerda.png').convert_alpha() 
sr_dio_img=pygame.image.load('Imagem/DIO_Socando_Direita.png').convert_alpha() 
sl_dio_img=pygame.image.load('Imagem/DIO_Socando_Esquerda.png').convert_alpha() 
ar_dio_img=pygame.image.load('Imagem/DIO_Atirando_Direita.png').convert_alpha() 
al_dio_img=pygame.image.load('Imagem/DIO_Atirando_Esquerda.png').convert_alpha() 
jl_dio_img=pygame.image.load('Imagem/DIO_pulando_esquerda.png').convert_alpha() 
jr_dio_img=pygame.image.load('Imagem/DIO_pulando_direita.png').convert_alpha()

pr_dio2_img=pygame.image.load('Imagem/DIO_Gold_Parado_Direita.png').convert_alpha() 
pl_dio2_img=pygame.image.load('Imagem/DIO_Gold_Parado_Esquerda.png').convert_alpha() 
sr_dio2_img=pygame.image.load('Imagem/DIO_Gold_Socando_Direita.png').convert_alpha() 
sl_dio2_img=pygame.image.load('Imagem/DIO_Gold_Socando_Esquerda.png').convert_alpha() 
ar_dio2_img=pygame.image.load('Imagem/DIO_Gold_Atirando_Direita.png').convert_alpha() 
al_dio2_img=pygame.image.load('Imagem/DIO_Gold_Atirando_Esquerda.png').convert_alpha() 
jl_dio2_img=pygame.image.load('Imagem/DIO_Gold_pulando_esquerda.png').convert_alpha() 
jr_dio2_img=pygame.image.load('Imagem/DIO_Gold_pulando_direita.png').convert_alpha() 

pr_wolf_img = pygame.image.load('Imagem/Were_Wolf_Parado_Direita.png').convert_alpha()
pl_wolf_img = pygame.image.load('Imagem/Were_Wolf_Parado_Esquerda.png').convert_alpha()
sr_wolf_img = pygame.image.load('Imagem/Were_Wolf_Socando_Direita.png').convert_alpha()
sl_wolf_img = pygame.image.load('Imagem/Were_Wolf_Socando_Esquerda.png').convert_alpha()
ar_wolf_img = pygame.image.load('Imagem/Were_Wolf_Atirando_Direita.png').convert_alpha()
al_wolf_img = pygame.image.load('Imagem/Were_Wolf_Atirando_Esquerda.png').convert_alpha()
jr_wolf_img = pygame.image.load('Imagem/Were_Wolf_Pulando_Direita.png').convert_alpha()
jl_wolf_img = pygame.image.load('Imagem/Were_Wolf_Pulando_Esquerda.png').convert_alpha()

pr_wolf2_img = pygame.image.load('Imagem/Were_Wolf_Gold_Parado_Direita.png').convert_alpha() 
pl_wolf2_img = pygame.image.load('Imagem/Were_Wolf_Gold_Parado_Esquerda.png').convert_alpha()
sr_wolf2_img = pygame.image.load('Imagem/Were_Wolf_Gold_Socando_Direita.png').convert_alpha()
sl_wolf2_img = pygame.image.load('Imagem/Were_Wolf_Gold_Socando_Esquerda.png').convert_alpha()
ar_wolf2_img = pygame.image.load('Imagem/Were_Wolf_Gold_Atirando_Direita.png').convert_alpha()
al_wolf2_img = pygame.image.load('Imagem/Were_Wolf_Gold_Atirando_Esquerda.png').convert_alpha()
jr_wolf2_img = pygame.image.load('Imagem/Were_Wolf_Gold_Pulando_Direita.png').convert_alpha()
jl_wolf2_img = pygame.image.load('Imagem/Were_Wolf_Gold_Pulando_Esquerda.png').convert_alpha()

pl_humb_img=pygame.image.load('Imagem/Humberto_Parado_Esquerda.png').convert_alpha()
pr_humb_img=pygame.image.load('Imagem/Humberto_Parado_Direita.png').convert_alpha()
sl_humb_img=pygame.image.load('Imagem/Humberto_Socando_Esquerda.png').convert_alpha()
sr_humb_img=pygame.image.load('Imagem/Humberto_Socando_Direita.png').convert_alpha()
al_humb_img=pygame.image.load('Imagem/Humberto_Atirando_Esquerda.png').convert_alpha()
ar_humb_img=pygame.image.load('Imagem/Humberto_Atirando_Direita.png').convert_alpha()
jl_humb_img=pygame.image.load('Imagem/Humberto_Pulando_Esquerda.png').convert_alpha()
jr_humb_img=pygame.image.load('Imagem/Humberto_Pulando_Direita.png').convert_alpha()

pl_humb2_img=pygame.image.load('Imagem/Humberto_Gold_Parado_Esquerda.png').convert_alpha()
pr_humb2_img=pygame.image.load('Imagem/Humberto_Gold_Parado_Direita.png').convert_alpha()
sl_humb2_img=pygame.image.load('Imagem/Humberto_Gold_Socando_Esquerda.png').convert_alpha()
sr_humb2_img=pygame.image.load('Imagem/Humberto_Gold_Socando_Direita.png').convert_alpha()
al_humb2_img=pygame.image.load('Imagem/Humberto_Gold_Atirando_Esquerda.png').convert_alpha()
ar_humb2_img=pygame.image.load('Imagem/Humberto_Gold_Atirando_Direita.png').convert_alpha()
jl_humb2_img=pygame.image.load('Imagem/Humberto_Gold_Pulando_Esquerda.png').convert_alpha()
jr_humb2_img=pygame.image.load('Imagem/Humberto_Gold_Pulando_Direita.png').convert_alpha()

pl_honda_img=pygame.image.load('Imagem/Honda_Parado_Esquerda.png').convert_alpha()
pr_honda_img=pygame.image.load('Imagem/Honda_Parado_Direita.png').convert_alpha()
sl_honda_img=pygame.image.load('Imagem/Honda_Socando_Esquerda.png').convert_alpha()
sr_honda_img=pygame.image.load('Imagem/Honda_Socando_Direita.png').convert_alpha()
al_honda_img=pygame.image.load('Imagem/Honda_Atirando_Esquerda.png').convert_alpha()
ar_honda_img=pygame.image.load('Imagem/Honda_Atirando_Direita.png').convert_alpha()
jl_honda_img=pygame.image.load('Imagem/Honda_Pulando_Esquerda.png').convert_alpha()
jr_honda_img=pygame.image.load('Imagem/Honda_Pulando_Direita.png').convert_alpha()

pl_honda2_img=pygame.image.load('Imagem/Honda_Gold_Parado_Esquerda.png').convert_alpha()
pr_honda2_img=pygame.image.load('Imagem/Honda_Gold_Parado_Direita.png').convert_alpha()
sl_honda2_img=pygame.image.load('Imagem/Honda_Gold_Socando_Esquerda.png').convert_alpha()
sr_honda2_img=pygame.image.load('Imagem/Honda_Gold_Socando_Direita.png').convert_alpha()
al_honda2_img=pygame.image.load('Imagem/Honda_Gold_Atirando_Esquerda.png').convert_alpha()
ar_honda2_img=pygame.image.load('Imagem/Honda_Gold_Atirando_Direita.png').convert_alpha()
jl_honda2_img=pygame.image.load('Imagem/Honda_Gold_Pulando_Esquerda.png').convert_alpha()
jr_honda2_img=pygame.image.load('Imagem/Honda_Gold_Pulando_Direita.png').convert_alpha()

pr_yoshi_img=pygame.image.load('Imagem/Yoshi_Parado_Direita.png').convert_alpha() 
pl_yoshi_img=pygame.image.load('Imagem/Yoshi_Parado_Esquerda.png').convert_alpha() 
sr_yoshi_img=pygame.image.load('Imagem/Yoshi_Socando_Direita.png').convert_alpha() 
sl_yoshi_img=pygame.image.load('Imagem/Yoshi_Socando_Esquerda.png').convert_alpha() 
ar_yoshi_img=pygame.image.load('Imagem/Yoshi_Atirando_Direita.png').convert_alpha() 
al_yoshi_img=pygame.image.load('Imagem/Yoshi_Atirando_Esquerda.png').convert_alpha() 
jl_yoshi_img=pygame.image.load('Imagem/Yoshi_pulando_esquerda.png').convert_alpha() 
jr_yoshi_img=pygame.image.load('Imagem/Yoshi_pulando_direita.png').convert_alpha()

pr_yoshi2_img=pygame.image.load('Imagem/Yoshi_Gold_Parado_Direita.png').convert_alpha() 
pl_yoshi2_img=pygame.image.load('Imagem/Yoshi_Gold_Parado_Esquerda.png').convert_alpha() 
sr_yoshi2_img=pygame.image.load('Imagem/Yoshi_Gold_Socando_Direita.png').convert_alpha() 
sl_yoshi2_img=pygame.image.load('Imagem/Yoshi_Gold_Socando_Esquerda.png').convert_alpha() 
ar_yoshi2_img=pygame.image.load('Imagem/Yoshi_Gold_Atirando_Direita.png').convert_alpha() 
al_yoshi2_img=pygame.image.load('Imagem/Yoshi_Gold_Atirando_Esquerda.png').convert_alpha() 
jl_yoshi2_img=pygame.image.load('Imagem/Yoshi_Gold_pulando_esquerda.png').convert_alpha() 
jr_yoshi2_img=pygame.image.load('Imagem/Yoshi_Gold_pulando_direita.png').convert_alpha()

pr_link_img=pygame.image.load('Imagem/Link_Parado_Direita.png').convert_alpha() 
pl_link_img=pygame.image.load('Imagem/Link_Parado_Esquerda.png').convert_alpha() 
sr_link_img=pygame.image.load('Imagem/Link_Socando_Direita.png').convert_alpha() 
sl_link_img=pygame.image.load('Imagem/Link_Socando_Esquerda.png').convert_alpha() 
ar_link_img=pygame.image.load('Imagem/Link_Atirando_Direita.png').convert_alpha() 
al_link_img=pygame.image.load('Imagem/Link_Atirando_Esquerda.png').convert_alpha() 
jl_link_img=pygame.image.load('Imagem/Link_pulando_esquerda.png').convert_alpha() 
jr_link_img=pygame.image.load('Imagem/Link_pulando_direita.png').convert_alpha()

pr_dino_img=pygame.image.load('Imagem/Dino_Parado_Direita.png').convert_alpha() 
pl_dino_img=pygame.image.load('Imagem/Dino_Parado_Esquerda.png').convert_alpha() 
sr_dino_img=pygame.image.load('Imagem/Dino_Socando_Direita.png').convert_alpha() 
sl_dino_img=pygame.image.load('Imagem/Dino_Socando_Esquerda.png').convert_alpha() 
ar_dino_img=pygame.image.load('Imagem/Dino_Atirando_Direita.png').convert_alpha() 
al_dino_img=pygame.image.load('Imagem/Dino_Atirando_Esquerda.png').convert_alpha() 
jl_dino_img=pygame.image.load('Imagem/Dino_pulando_esquerda.png').convert_alpha() 
jr_dino_img=pygame.image.load('Imagem/Dino_pulando_direita.png').convert_alpha()

pr_dino2_img=pygame.image.load('Imagem/Dino_Gold_Parado_Direita.png').convert_alpha() 
pl_dino2_img=pygame.image.load('Imagem/Dino_Gold_Parado_Esquerda.png').convert_alpha() 
sr_dino2_img=pygame.image.load('Imagem/Dino_Gold_Socando_Direita.png').convert_alpha() 
sl_dino2_img=pygame.image.load('Imagem/Dino_Gold_Socando_Esquerda.png').convert_alpha() 
ar_dino2_img=pygame.image.load('Imagem/Dino_Gold_Atirando_Direita.png').convert_alpha() 
al_dino2_img=pygame.image.load('Imagem/Dino_Gold_Atirando_Esquerda.png').convert_alpha() 
jl_dino2_img=pygame.image.load('Imagem/Dino_Gold_pulando_esquerda.png').convert_alpha() 
jr_dino2_img=pygame.image.load('Imagem/Dino_Gold_pulando_direita.png').convert_alpha()

fogo_lobo_esquerda_img=pygame.image.load('Imagem/Poder_Lobo_Esquerda.png').convert_alpha()
fogo_lobo_direita_img=pygame.image.load('Imagem/Poder_Lobo_Direita.png').convert_alpha()
fogo_esquerda_img=pygame.image.load('Imagem/Poder_Fogo_Esquerda.png').convert_alpha()
fogo_direita_img=pygame.image.load('Imagem/Poder_Fogo_Direita.png').convert_alpha()
faca_esquerda_img=pygame.image.load('Imagem/Poder_Faca_Esquerda.png').convert_alpha()
faca_direita_img=pygame.image.load('Imagem/Poder_Faca_Direita.png').convert_alpha()
cerveja_direita_img=pygame.image.load('Imagem/Poder_Cerveja_Direita.png').convert_alpha()
cerveja_esquerda_img=pygame.image.load('Imagem/Poder_Cerveja_Esquerda.png').convert_alpha()
ovo_esquerda_img=pygame.image.load('Imagem/Poder_Ovo_Esquerda.png').convert_alpha()
ovo_direita_img=pygame.image.load('Imagem/Poder_Ovo_Direita.png').convert_alpha()
meteoro_esquerda_img=pygame.image.load('Imagem/Poder_Dino_Esquerda.png').convert_alpha()
meteoro_direita_img=pygame.image.load('Imagem/Poder_Dino_Direita.png').convert_alpha()
flecha_esquerda_img=pygame.image.load('Imagem/Poder_Flecha_Esquerda.png').convert_alpha()
flecha_direita_img=pygame.image.load('Imagem/Poder_Flecha_Direita.png').convert_alpha()

background_img = pygame.image.load('Imagem/cenário.jpg').convert_alpha()
background2_img = pygame.image.load('Imagem/Background2.png').convert_alpha()
background3_img = pygame.image.load('Imagem/Background3.png').convert_alpha()
background4_img = pygame.image.load('Imagem/Background4.png').convert_alpha()
background5_img = pygame.image.load('Imagem/3XOka2Q - Imgur.gif').convert_alpha()
teladopersonagemsecreto_img = pygame.image.load('Imagem/teladopersonagemsecreto.png').convert_alpha()
barradefundo_img = pygame.image.load('Imagem/Fundo branco.png').convert_alpha()
barraverde1_img = pygame.image.load('Imagem/barraverde.png').convert_alpha()
barravermelha1_img = pygame.image.load('Imagem/barravermelha.png').convert_alpha()
barradevida1_img = pygame.image.load('Imagem/barradevida.png').convert_alpha()
barraverde2_img = pygame.image.load('Imagem/barraverde.png').convert_alpha()
barravermelha2_img = pygame.image.load('Imagem/barravermelha.png').convert_alpha()
barradevida2_img = pygame.image.load('Imagem/barradevida.png').convert_alpha()
barraverde_img = pygame.image.load('Imagem/barraverde.png').convert_alpha()
barravermelha_img = pygame.image.load('Imagem/barravermelha.png').convert_alpha()
barradevida_img = pygame.image.load('Imagem/barradevida.png').convert_alpha()
barradevidacomvitorias_img = pygame.image.load('Imagem/barradevidacomvitorias.png').convert_alpha()

pr_dio_img=pygame.transform.scale(pr_dio_img, (180, P1_HEIGHT+30))
pl_dio_img=pygame.transform.scale(pl_dio_img, (180, P1_HEIGHT+30))
sr_dio_img=pygame.transform.scale(sr_dio_img, (180, P1_HEIGHT+30))
sl_dio_img=pygame.transform.scale(sl_dio_img, (180, P1_HEIGHT+30))
ar_dio_img=pygame.transform.scale(ar_dio_img, (200, P1_HEIGHT+30))
al_dio_img=pygame.transform.scale(al_dio_img, (200, P1_HEIGHT+30))
jl_dio_img=pygame.transform.scale(jl_dio_img, (200, P1_HEIGHT+30))
jr_dio_img=pygame.transform.scale(jr_dio_img, (200, P1_HEIGHT+30))

pr_dio2_img=pygame.transform.scale(pr_dio2_img, (200, P1_HEIGHT+30))
pl_dio2_img=pygame.transform.scale(pl_dio2_img, (200, P1_HEIGHT+30))
sr_dio2_img=pygame.transform.scale(sr_dio2_img, (200, P1_HEIGHT+30))
sl_dio2_img=pygame.transform.scale(sl_dio2_img, (200, P1_HEIGHT+30))
ar_dio2_img=pygame.transform.scale(ar_dio2_img, (200, P1_HEIGHT+30))
al_dio2_img=pygame.transform.scale(al_dio2_img, (200, P1_HEIGHT+30))
jl_dio2_img=pygame.transform.scale(jl_dio2_img, (200, P1_HEIGHT+30))
jr_dio2_img=pygame.transform.scale(jr_dio2_img, (200, P1_HEIGHT+30))

pr_wolf_img=pygame.transform.scale(pr_wolf_img, (P1_WIDTH, P1_HEIGHT+30))
pl_wolf_img=pygame.transform.scale(pl_wolf_img, (P1_WIDTH, P1_HEIGHT+30))
sr_wolf_img=pygame.transform.scale(sr_wolf_img, (P1_WIDTH+30, P1_HEIGHT+30))
sl_wolf_img=pygame.transform.scale(sl_wolf_img, (P1_WIDTH+30, P1_HEIGHT+30))
ar_wolf_img=pygame.transform.scale(ar_wolf_img, (P1_WIDTH+30, P1_HEIGHT+30))
al_wolf_img=pygame.transform.scale(al_wolf_img, (P1_WIDTH+30, P1_HEIGHT+30))
jr_wolf_img=pygame.transform.scale(jr_wolf_img, (P1_WIDTH+30, P1_HEIGHT+30))
jl_wolf_img=pygame.transform.scale(jl_wolf_img, (P1_WIDTH+30, P1_HEIGHT+30))

pr_wolf2_img=pygame.transform.scale(pr_wolf2_img, (P1_WIDTH, P1_HEIGHT+30))
pl_wolf2_img=pygame.transform.scale(pl_wolf2_img, (P1_WIDTH, P1_HEIGHT+30))
sr_wolf2_img=pygame.transform.scale(sr_wolf2_img, (P1_WIDTH+40, P1_HEIGHT+60))
sl_wolf2_img=pygame.transform.scale(sl_wolf2_img, (P1_WIDTH+40, P1_HEIGHT+60))
ar_wolf2_img=pygame.transform.scale(ar_wolf2_img, (P1_WIDTH+30, P1_HEIGHT+30))
al_wolf2_img=pygame.transform.scale(al_wolf2_img, (P1_WIDTH+30, P1_HEIGHT+30))
jr_wolf2_img=pygame.transform.scale(jr_wolf2_img, (P1_WIDTH, P1_HEIGHT-10))
jl_wolf2_img=pygame.transform.scale(jl_wolf2_img, (P1_WIDTH, P1_HEIGHT-10))

pl_humb_img=pygame.transform.scale(pl_humb_img, (P1_WIDTH, P1_HEIGHT+30))
pr_humb_img=pygame.transform.scale(pr_humb_img, (P1_WIDTH, P1_HEIGHT+30))
sl_humb_img=pygame.transform.scale(sl_humb_img, (200+30, P1_HEIGHT+30))
sr_humb_img=pygame.transform.scale(sr_humb_img, (200+30, P1_HEIGHT+30))
al_humb_img=pygame.transform.scale(al_humb_img, (200+30, P1_HEIGHT+30))
ar_humb_img=pygame.transform.scale(ar_humb_img, (200+30, P1_HEIGHT+30))
jl_humb_img=pygame.transform.scale(jl_humb_img, (180, P1_HEIGHT+30))
jr_humb_img=pygame.transform.scale(jr_humb_img, (180, P1_HEIGHT+30))

pl_humb2_img=pygame.transform.scale(pl_humb2_img, (150, P1_HEIGHT+30))
pr_humb2_img=pygame.transform.scale(pr_humb2_img, (150, P1_HEIGHT+30))
sl_humb2_img=pygame.transform.scale(sl_humb2_img, (180+30, P1_HEIGHT+30))
sr_humb2_img=pygame.transform.scale(sr_humb2_img, (200+30, P1_HEIGHT+30))
al_humb2_img=pygame.transform.scale(al_humb2_img, (200+30, P1_HEIGHT+30))
ar_humb2_img=pygame.transform.scale(ar_humb2_img, (200+30, P1_HEIGHT+30))
jl_humb2_img=pygame.transform.scale(jl_humb2_img, (180, P1_HEIGHT+30))
jr_humb2_img=pygame.transform.scale(jr_humb2_img, (180, P1_HEIGHT+30))

pr_honda_img=pygame.transform.scale(pr_honda_img, (P1_WIDTH, P1_HEIGHT+30))
pl_honda_img=pygame.transform.scale(pl_honda_img, (P1_WIDTH, P1_HEIGHT+30))
sr_honda_img=pygame.transform.scale(sr_honda_img, (P1_WIDTH+30, P1_HEIGHT+30))
sl_honda_img=pygame.transform.scale(sl_honda_img, (P1_WIDTH+30, P1_HEIGHT+30))
ar_honda_img=pygame.transform.scale(ar_honda_img, (P1_WIDTH+30, P1_HEIGHT+30))
al_honda_img=pygame.transform.scale(al_honda_img, (P1_WIDTH+30, P1_HEIGHT+30))
jr_honda_img=pygame.transform.scale(jr_honda_img, (P1_WIDTH+30, P1_HEIGHT+30))
jl_honda_img=pygame.transform.scale(jl_honda_img, (P1_WIDTH+30, P1_HEIGHT+30))

pr_honda2_img=pygame.transform.scale(pr_honda2_img, (P1_WIDTH, P1_HEIGHT+30))
pl_honda2_img=pygame.transform.scale(pl_honda2_img, (P1_WIDTH, P1_HEIGHT+30))
sr_honda2_img=pygame.transform.scale(sr_honda2_img, (P1_WIDTH+30, P1_HEIGHT+30))
sl_honda2_img=pygame.transform.scale(sl_honda2_img, (P1_WIDTH+30, P1_HEIGHT+30))
ar_honda2_img=pygame.transform.scale(ar_honda2_img, (P1_WIDTH+30, P1_HEIGHT+30))
al_honda2_img=pygame.transform.scale(al_honda2_img, (P1_WIDTH+30, P1_HEIGHT+30))
jr_honda2_img=pygame.transform.scale(jr_honda2_img, (P1_WIDTH+30, P1_HEIGHT+30))
jl_honda2_img=pygame.transform.scale(jl_honda2_img, (P1_WIDTH+30, P1_HEIGHT+30))

pl_yoshi_img=pygame.transform.scale(pl_yoshi_img, (P1_WIDTH, P1_HEIGHT))
pr_yoshi_img=pygame.transform.scale(pr_yoshi_img, (P1_WIDTH, P1_HEIGHT))
sl_yoshi_img=pygame.transform.scale(sl_yoshi_img, (200, P1_HEIGHT))
sr_yoshi_img=pygame.transform.scale(sr_yoshi_img, (200, P1_HEIGHT))
al_yoshi_img=pygame.transform.scale(al_yoshi_img, (200, P1_HEIGHT))
ar_yoshi_img=pygame.transform.scale(ar_yoshi_img, (200, P1_HEIGHT))
jl_yoshi_img=pygame.transform.scale(jl_yoshi_img, (180, P1_HEIGHT-20))
jr_yoshi_img=pygame.transform.scale(jr_yoshi_img, (180, P1_HEIGHT-20))

pl_yoshi2_img=pygame.transform.scale(pl_yoshi2_img, (P1_WIDTH, P1_HEIGHT))
pr_yoshi2_img=pygame.transform.scale(pr_yoshi2_img, (P1_WIDTH, P1_HEIGHT))
sl_yoshi2_img=pygame.transform.scale(sl_yoshi2_img, (200, P1_HEIGHT))
sr_yoshi2_img=pygame.transform.scale(sr_yoshi2_img, (200, P1_HEIGHT))
al_yoshi2_img=pygame.transform.scale(al_yoshi2_img, (200, P1_HEIGHT))
ar_yoshi2_img=pygame.transform.scale(ar_yoshi2_img, (200, P1_HEIGHT))
jl_yoshi2_img=pygame.transform.scale(jl_yoshi2_img, (180, P1_HEIGHT-20))
jr_yoshi2_img=pygame.transform.scale(jr_yoshi2_img, (180, P1_HEIGHT-20))

pl_link_img=pygame.transform.scale(pl_link_img, (P1_WIDTH, P1_HEIGHT))
pr_link_img=pygame.transform.scale(pr_link_img, (P1_WIDTH, P1_HEIGHT))
sl_link_img=pygame.transform.scale(sl_link_img, (200, P1_HEIGHT))
sr_link_img=pygame.transform.scale(sr_link_img, (200, P1_HEIGHT))
al_link_img=pygame.transform.scale(al_link_img, (200, P1_HEIGHT))
ar_link_img=pygame.transform.scale(ar_link_img, (200, P1_HEIGHT))
jl_link_img=pygame.transform.scale(jl_link_img, (200, P1_HEIGHT))
jr_link_img=pygame.transform.scale(jr_link_img, (180, P1_HEIGHT))

pr_dino_img=pygame.transform.scale(pr_dino_img, (180, P1_HEIGHT+30))
pl_dino_img=pygame.transform.scale(pl_dino_img, (180, P1_HEIGHT+30))
sr_dino_img=pygame.transform.scale(sr_dino_img, (180, P1_HEIGHT+30))
sl_dino_img=pygame.transform.scale(sl_dino_img, (180, P1_HEIGHT+30))
ar_dino_img=pygame.transform.scale(ar_dino_img, (200, P1_HEIGHT+30))
al_dino_img=pygame.transform.scale(al_dino_img, (200, P1_HEIGHT+30))
jl_dino_img=pygame.transform.scale(jl_dino_img, (200, P1_HEIGHT+30))
jr_dino_img=pygame.transform.scale(jr_dino_img, (200, P1_HEIGHT+30))

pr_dino2_img=pygame.transform.scale(pr_dino2_img, (180, P1_HEIGHT+30))
pl_dino2_img=pygame.transform.scale(pl_dino2_img, (180, P1_HEIGHT+30))
sr_dino2_img=pygame.transform.scale(sr_dino2_img, (180, P1_HEIGHT+30))
sl_dino2_img=pygame.transform.scale(sl_dino2_img, (180, P1_HEIGHT+30))
ar_dino2_img=pygame.transform.scale(ar_dino2_img, (200, P1_HEIGHT+30))
al_dino2_img=pygame.transform.scale(al_dino2_img, (200, P1_HEIGHT+30))
jl_dino2_img=pygame.transform.scale(jl_dino2_img, (200, P1_HEIGHT+30))
jr_dino2_img=pygame.transform.scale(jr_dino2_img, (200, P1_HEIGHT+30))

fogo_lobo_esquerda_img=pygame.transform.scale(fogo_lobo_esquerda_img,(80,80))
fogo_lobo_direita_img=pygame.transform.scale(fogo_lobo_direita_img,(80,80))
fogo_esquerda_img=pygame.transform.scale(fogo_esquerda_img,(80,80))
fogo_direita_img=pygame.transform.scale(fogo_direita_img,(80,80))
faca_esquerda_img=pygame.transform.scale(faca_esquerda_img,(80,30))
faca_direita_img=pygame.transform.scale(faca_direita_img,(80,30))
cerveja_esquerda_img=pygame.transform.scale(cerveja_esquerda_img,(80,30))
cerveja_direita_img=pygame.transform.scale(cerveja_direita_img,(80,30))
ovo_esquerda_img=pygame.transform.scale(ovo_esquerda_img,(60,70))
ovo_direita_img=pygame.transform.scale(ovo_direita_img,(60,70))
meteoro_esquerda_img=pygame.transform.scale(meteoro_esquerda_img,(70,70))
meteoro_direita_img=pygame.transform.scale(meteoro_direita_img,(70,70))
flecha_esquerda_img=pygame.transform.scale(flecha_esquerda_img,(80,30))
flecha_direita_img=pygame.transform.scale(flecha_direita_img,(80,30))


background_img=pygame.transform.scale(background_img, (WIDTH, HEIGHT))
background2_img=pygame.transform.scale(background2_img, (WIDTH, HEIGHT))
background3_img=pygame.transform.scale(background3_img, (WIDTH, HEIGHT))
background4_img=pygame.transform.scale(background4_img, (WIDTH+30, HEIGHT))
background5_img=pygame.transform.scale(background5_img, (WIDTH+30, HEIGHT))
teladopersonagemsecreto_img=pygame.transform.scale(teladopersonagemsecreto_img , (WIDTH+30, HEIGHT))
barradefundo_img = pygame.transform.scale(barradefundo_img, (300, 40))
barradefundotempo_img = pygame.transform.scale(barradefundo_img, (60, 30))
barraverde1_img = pygame.transform.scale(barraverde1_img, (compbarraverd, 40))
barraverde2_img = pygame.transform.scale(barraverde2_img, (compbarraverd, 40))
barravermelha1_img = pygame.transform.scale(barravermelha1_img, (compbarraverm, 40))
barradevida1_img = pygame.transform.scale(barradevida1_img, (300, 60))
barravermelha2_img = pygame.transform.scale(barravermelha2_img, (compbarraverm, 40))
barradevida2_img = pygame.transform.scale(barradevida2_img, (300, 60))
barradevida_img = pygame.transform.scale(barradevida_img, (310, 60))
barradevidacomvitorias_img = pygame.transform.scale(barradevidacomvitorias_img, (311, 90))

imagens={
    #DIO
    1: [[faca_esquerda_img, faca_direita_img], [pl_dio_img, pr_dio_img], [pl_dio2_img, pr_dio2_img], [sl_dio_img, sr_dio_img], [sl_dio2_img, sr_dio2_img], [al_dio_img, ar_dio_img], [al_dio2_img, ar_dio2_img], [jl_dio_img, jr_dio_img], [jl_dio2_img, jr_dio2_img]],
    
    #Werewolf
    2: [[fogo_lobo_esquerda_img, fogo_lobo_direita_img], [pl_wolf_img, pr_wolf_img], [pl_wolf2_img, pr_wolf2_img], [sl_wolf_img, sr_wolf_img], [sl_wolf2_img, sr_wolf2_img], [al_wolf_img, ar_wolf_img], [al_wolf2_img, ar_wolf2_img], [jl_wolf_img, jr_wolf_img], [jl_wolf2_img, jr_wolf2_img]],
    
    #Humberto
    3: [[fogo_esquerda_img, fogo_direita_img],[pl_humb_img, pr_humb_img], [pl_humb2_img, pr_humb2_img], [sl_humb_img, sr_humb_img], [sl_humb2_img, sr_humb2_img], [al_humb_img, ar_humb_img], [al_humb2_img, ar_humb2_img], [jl_humb_img, jr_humb_img], [jl_humb2_img, jr_humb2_img]],
    
    #Honda
    4: [[cerveja_esquerda_img, cerveja_direita_img],[pl_honda_img, pr_honda_img], [pl_honda2_img, pr_honda2_img], [sl_honda_img, sr_honda_img], [sl_honda2_img, sr_honda2_img], [al_honda_img, ar_honda_img], [al_honda2_img, ar_honda2_img], [jl_honda_img, jr_honda_img], [jl_honda2_img, jr_honda2_img]],

    #Yoshi
    5: [[ovo_esquerda_img, ovo_direita_img],[pl_yoshi_img, pr_yoshi_img], [pl_yoshi2_img, pr_yoshi2_img], [sl_yoshi_img, sr_yoshi_img], [sl_yoshi2_img, sr_yoshi2_img], [al_yoshi_img, ar_yoshi_img], [al_yoshi2_img, ar_yoshi2_img], [jl_yoshi_img, jr_yoshi_img], [jl_yoshi2_img, jr_yoshi2_img]],

    #Link
    6: [[flecha_esquerda_img, flecha_direita_img],[pl_link_img, pr_link_img], [pl_link_img, pr_link_img], [sl_link_img, sr_link_img], [sl_link_img, sr_link_img], [al_link_img, ar_link_img], [al_link_img, ar_link_img], [jl_link_img, jr_link_img], [jl_link_img, jr_link_img]],
    #Dino Boxeador
    7: [[meteoro_esquerda_img, meteoro_direita_img],[pl_dino_img, pr_dino_img], [pl_dino2_img, pr_dino2_img], [sl_dino_img, sr_dino_img], [sl_dino2_img, sr_dino2_img], [al_dino_img, ar_dino_img], [al_dino2_img, ar_dino2_img], [jl_dino_img, jr_dino_img], [jl_dino2_img, jr_dino2_img]]

}

# Sons

pygame.mixer.music.load(os.path.join(SND_DIR, 'Musica_Inicio.mp3'))
pygame.mixer.music.set_volume(0.2)
dio_soco_sound = pygame.mixer.Sound(os.path.join(SND_DIR, 'Dio_Ataque.mp3'))
dio_soco_sound.set_volume(1.0)