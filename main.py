print("Criadores do projeto: Eduardo Selber Castanho, Henrique Fazzio Badin, Henrique Rocha Bomfim")
# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
from classes import *

pygame.init()

# ----- Gera tela principal
window = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption('Mortal Insper!')

# ----- Inicia estruturas de dados
game = True
p1_img=pygame.image.load('Projeto Final DesSoft/Projeto_Final_DesSoft/Imagem/Quadrado_Teste.png').convert_alpha()
p1_img=pygame.transform.scale(p1_img, (P1_WIDTH, P1_HEIGHT))
# ===== Loop principal =====
while game:
    #Cria jogadores
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False

    # ----- Gera saídas
    window.fill((0, 0, 0))  # Preenche com a cor preta

    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados

