import random
from time import sleep

def mostrar_tabuleiro(tab):
    for linha in tab:
        print(" | ".join(linha))
        print("-" * 9)


def verificar_vitoria(tab, jogador):
    #verifica as linhas
    for i in range(3):
        if tab[i][0] == jogador and tab[i][1] == jogador and tab[i][2] == jogador:
            return True

    #verifica as colunas   
    for i in range(3):
        if tab[0][i] == jogador and tab[1][i] == jogador and tab[2][i] == jogador:
            return True
    
    #verifica as diagonais
    if (tab[0][0] == jogador and tab[1][1] == jogador and tab[2][2] == jogador) or (tab[0][2] == jogador and tab[1][1] == jogador and tab[2][0] == jogador):
        return True

    return False


tabuleiro = [[' ',' ',' '], 
             [' ',' ',' '], 
             [' ',' ',' ']]

jogador_atual = "X"

for rodada in range(9):
    mostrar_tabuleiro(tabuleiro)
    if jogador_atual == "X":
        escolha = input(f"Jogador {jogador_atual} escolha uma posição de 1 à 9: ")
        pos = int(escolha) - 1
    else:
        print("Vez do Computador...")
        posicoes_livres = [i for i in range(9) if tabuleiro[i // 3][i % 3] == ' ']
        pos = random.choice(posicoes_livres)
        sleep(2)
        print(f"Computador escolheu a posição {pos + 1}")

    linha, coluna = pos //3, pos %3

    if tabuleiro[linha][coluna] in ["X", "O"]:
        print("Posição já ocupada. Tente Outra Vez!!")
        continue

    tabuleiro[linha][coluna] = jogador_atual

    if verificar_vitoria(tabuleiro, jogador_atual):
        mostrar_tabuleiro(tabuleiro)
        print(f'Jogador {jogador_atual} venceu!! Parabéns')
        break


    if jogador_atual == "O":
        jogador_atual = "X"
    else:
        jogador_atual= "O"

else:
    mostrar_tabuleiro(tabuleiro)
    print("Empate! Ninguém venceu.")