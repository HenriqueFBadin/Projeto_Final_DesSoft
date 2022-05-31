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
#jl_humb2_img=pygame.image.load('Imagem/Humberto_Gold_Pulando_Esquerda.png').convert_alpha()
#jr_humb2_img=pygame.image.load('Imagem/Humberto_Gold_Pulando_Direita.png').convert_alpha()

pr_wolf_img = pygame.image.load('Imagem/Werewolf_Parado_Direita.png').convert_alpha()
pl_wolf_img = pygame.image.load('Imagem/Werewolf_Parado_Esquerda.png').convert_alpha()
sr_wolf_img = pygame.image.load('Imagem/Werewolf_Socando_Direita.png').convert_alpha()
sl_wolf_img = pygame.image.load('Imagem/Werewolf_Socando_Esquerda.png').convert_alpha()
pr_wolf2_img = pygame.image.load('Imagem/Werewolf_Gold_Parado_Direita.png').convert_alpha() 
pl_wolf2_img = pygame.image.load('Imagem/Werewolf_Gold_Parado_Esquerda.png').convert_alpha()

gelo_esquerda_img=pygame.image.load('Imagem/Poder_Gelo_Esquerda.png').convert_alpha()
gelo_direita_img=pygame.image.load('Imagem/Poder_Gelo_Direita.png').convert_alpha()
fogo_esquerda_img=pygame.image.load('Imagem/Poder_Fogo_Esquerda.png').convert_alpha()
fogo_direita_img=pygame.image.load('Imagem/Poder_Fogo_Direita.png').convert_alpha()
faca_esquerda_img=pygame.image.load('Imagem/Poder_Faca_Esquerda.png').convert_alpha()
faca_direita_img=pygame.image.load('Imagem/Poder_Faca_Direita.png').convert_alpha()

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

pr_dio2_img=pygame.image.load('Imagem/DIO_Gold_Parado_Direita.png').convert_alpha() 
pl_dio2_img=pygame.image.load('Imagem/DIO_Gold_Parado_Esquerda.png').convert_alpha() 
sr_dio2_img=pygame.image.load('Imagem/DIO_Gold_Socando_Direita.png').convert_alpha() 
sl_dio2_img=pygame.image.load('Imagem/DIO_Gold_Socando_Esquerda.png').convert_alpha() 
ar_dio2_img=pygame.image.load('Imagem/DIO_Gold_Atirando_Direita.png').convert_alpha() 
al_dio2_img=pygame.image.load('Imagem/DIO_Gold_Atirando_Esquerda.png').convert_alpha() 
jl_dio2_img=pygame.image.load('Imagem/DIO_Gold_pulando_esquerda.png').convert_alpha() 
jr_dio2_img=pygame.image.load('Imagem/DIO_Gold_pulando_direita.png').convert_alpha() 

pr_wolf_img=pygame.transform.scale(pr_wolf_img, (P1_WIDTH, P1_HEIGHT+30))
pl_wolf_img=pygame.transform.scale(pl_wolf_img, (P1_WIDTH, P1_HEIGHT+30))
pr_wolf2_img=pygame.transform.scale(pr_wolf2_img, (P1_WIDTH, P1_HEIGHT+30))
pl_wolf2_img=pygame.transform.scale(pl_wolf2_img, (P1_WIDTH, P1_HEIGHT+30))
sr_wolf_img=pygame.transform.scale(sr_wolf_img, (P1_WIDTH+30, P1_HEIGHT+30))
sl_wolf_img=pygame.transform.scale(sl_wolf_img, (P1_WIDTH+30, P1_HEIGHT+30))

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
#jl_humb2_img=pygame.transform.scale(jl_humb_img, (180, P1_HEIGHT+30))
#jr_humb2_img=pygame.transform.scale(jr_humb_img, (180, P1_HEIGHT+30))


pr_dio_img=pygame.transform.scale(pr_dio_img, (180, P1_HEIGHT+30))
pl_dio_img=pygame.transform.scale(pl_dio_img, (180, P1_HEIGHT+30))
sr_dio_img=pygame.transform.scale(sr_dio_img, (180, P1_HEIGHT+30))
sl_dio_img=pygame.transform.scale(sl_dio_img, (180, P1_HEIGHT+30))
ar_dio_img=pygame.transform.scale(ar_dio_img, (200, P1_HEIGHT+30))
al_dio_img=pygame.transform.scale(al_dio_img, (200, P1_HEIGHT+30))
jl_dio_img=pygame.transform.scale(jl_dio_img, (200, P1_HEIGHT+30))
jr_dio_img=pygame.transform.scale(jr_dio_img, (200, P1_HEIGHT+30))

pr_dio2_img=pygame.transform.scale(pr_dio2_img, (180, P1_HEIGHT+30))
pl_dio2_img=pygame.transform.scale(pl_dio2_img, (180, P1_HEIGHT+30))
sr_dio2_img=pygame.transform.scale(sr_dio2_img, (180, P1_HEIGHT+30))
sl_dio2_img=pygame.transform.scale(sl_dio2_img, (180, P1_HEIGHT+30))
ar_dio2_img=pygame.transform.scale(ar_dio2_img, (180, P1_HEIGHT+30))
al_dio2_img=pygame.transform.scale(al_dio2_img, (180, P1_HEIGHT+30))
jl_dio2_img=pygame.transform.scale(jl_dio2_img, (200, P1_HEIGHT+30))
jr_dio2_img=pygame.transform.scale(jr_dio2_img, (200, P1_HEIGHT+30))

gelo_esquerda_img=pygame.transform.scale(gelo_esquerda_img,(80,80))
gelo_direita_img=pygame.transform.scale(gelo_direita_img,(80,80))
fogo_esquerda_img=pygame.transform.scale(fogo_esquerda_img,(80,80))
fogo_direita_img=pygame.transform.scale(fogo_direita_img,(80,80))
faca_esquerda_img=pygame.transform.scale(faca_esquerda_img,(80,30))
faca_direita_img=pygame.transform.scale(faca_direita_img,(80,30))

background_img=pygame.transform.scale(background_img, (WIDTH, HEIGHT))
background2_img=pygame.transform.scale(background2_img, (WIDTH, HEIGHT))
background3_img=pygame.transform.scale(background3_img, (WIDTH, HEIGHT))
background4_img=pygame.transform.scale(background4_img, (WIDTH+30, HEIGHT))

imagens={
    #DIO
    1: [[faca_esquerda_img, faca_direita_img], [pl_dio_img, pr_dio_img], [pl_dio2_img, pr_dio2_img], [sl_dio_img, sr_dio_img], [sl_dio2_img, sr_dio2_img], [al_dio_img, ar_dio_img], [al_dio2_img, ar_dio2_img], [jl_dio_img, jr_dio_img], [jl_dio2_img, jr_dio2_img]],
    
    #Werewolf
    2: {},
    
    #Humberto
    3: [[fogo_esquerda_img, fogo_direita_img],[pl_humb_img, pr_humb_img], [pl_humb2_img, pr_humb2_img], [sl_humb_img, sr_humb_img], [sl_humb2_img, sr_humb2_img], [al_humb_img, ar_humb_img], [al_humb2_img, ar_humb2_img], [jl_humb_img, jr_humb_img], [jl_humb_img, jr_humb_img]]
}