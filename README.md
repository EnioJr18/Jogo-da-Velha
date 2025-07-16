# Jogo da Velha em Python
### Este projeto implementa um simples Jogo da Velha (Tic-Tac-Toe) em Python, onde o jogador humano enfrenta o computador.

##### Como funciona:
* O tabuleiro é uma matriz 3x3, representada por uma lista de listas.
* O jogador humano joga com "X" e escolhe a posição digitando um número de 1 a 9.
* O computador joga com "O" e escolhe uma posição livre aleatoriamente usando a biblioteca random.
* Após cada jogada, o tabuleiro é exibido.
* O código verifica se houve vitória nas linhas, colunas ou diagonais após cada jogada.
* Se alguém vencer, o jogo termina e exibe o vencedor.
* Se todas as posições forem preenchidas sem vencedor, o jogo termina em empate.

##### Principais funções:
* mostrar_tabuleiro(tab): Exibe o tabuleiro formatado no console.
* verificar_vitoria(tab, jogador): Verifica se o jogador atual venceu, analisando linhas, colunas e diagonais.

##### Como jogar:
* Execute o script em Python.
* O jogador humano começa, digitando a posição desejada (de 1 a 9).
* O computador faz sua jogada automaticamente.
* O jogo alterna entre os jogadores até que alguém vença ou ocorra empate.
