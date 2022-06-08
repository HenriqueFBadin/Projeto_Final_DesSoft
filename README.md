# Projeto_Final_DesSoft

Repositório para o Projeto Final da matéria de DesSoft:https://github.com/HenriqueFBadin/Projeto_Final_DesSoft.git
O grupo é composto pelos alunos Henrique Badin, Henrique Bomfim e Eduardo Selber da sala 1A de Engenharia do Insper.

Link do vídeo sobre o jogo, no estilo trailer: https://youtu.be/SpFoWM9AOd8

O arquivo python que se deve rodar para jogar o jogo se chama jogo.py

Para o player jogar, primeiro é necessário a instalação da biblioteca do pygame.

O jogo Mortal Insper é um PvP, player versus player, do genero de Luta. Esse jogo inclui uma seleção de 6 personagens diversos, abrangendo personagens como o Humbertor, professor de programação do Insper responsável pela matéria de Design de Software, e um dinossauro boxeador. Para selecionar os personagens é necessário clicar com o botão esquerdo do mouse na imagem do personagem desejado na tela de selção dos personagens, que é que vem logo em seguida da tela inicial. O jogador 1 escolhe os personagens da esquerda enquanto o jogador 2 escolhe os da direita da tela de seleção. 

Durante o jogo, para o player 1 movimentar-se é necessario pressionar as teclas 'd', para se movimentar para a direita,'a', para se mover para a esquerda e 'w' para pular. Para atacar é necessário pressionar a tecla 'c' para socar o adversário, enquanto o 'v' lança um poder de longa distancia. De maneira análoga, o player 2 precisa pressionar a Seta direita, Seta esquerda e Seta para cima para se movimentar, ',' e 'l' para atacar. 

Além disso, o jogo utiliza um sistema de 3 rounds, em que o vencedor é aquele que ganhar 2 rounds primeiro, além de que para ganhar um round em específico precisa reduzir a vida do outro player, que pode ser observado no topo da tela, para zero. Essa vitória em específica também é alcançada quando  o timer, que fica no topo da tela, zera e será declarado vencedor àquele que tiver com mais vida. 

Para finalizar as funcionalidades do jogo, quando um personagem atingir 50% da vida ativa o segundo estágio dele, representado por uma mudança visual, que lhe atribui um buff de status. Assim, compilando todas as funcionalidades presentes nesse documento obtem-se o jogo Mortal Insper.  