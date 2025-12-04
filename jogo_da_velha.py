import random
import os
import time

COR_X = '\033[91m'  
COR_O = '\033[96m'  
RESET = '\033[0m'   


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def mostrar_tabuleiro(tab):
    limpar_tela()
    print("=== JOGO DA VELHA ===\n")

    for i, linha in enumerate(tab):
        linha_formatada = " | ".join(linha)
        print(f" {linha_formatada} ")

        if i < 2:
            print("-" * 11)
    print("\n")


def verificar_vitoria(tab, jogador):
    for i in range(3):
        if tab[i][0] == jogador and tab[i][1] == jogador and tab[i][2] == jogador:
            return True

        if tab[0][i] == jogador and tab[1][i] == jogador and tab[2][i] == jogador:
            return True

    if tab[0][0] == jogador and tab[1][1] == jogador and tab[2][2] == jogador:
        return True
    if tab[0][2] == jogador and tab[1][1] == jogador and tab[2][0] == jogador:
        return True

    return False


def tabuleiro_cheio(tab):
    for linha in tab:
        for item in linha:
            if item != 'X' and item != 'O' and item not in [COR_X+'X'+RESET, COR_O+'O'+RESET]:
                return False
    return True


def jogar():
    while True:
        tabuleiro = [['1', '2', '3'],
                     ['4', '5', '6'],
                     ['7', '8', '9']]

        jogador_atual = "X"
        rodadas = 0
        jogo_ativo = True

        while jogo_ativo:
            mostrar_tabuleiro(tabuleiro)

            if jogador_atual == "X":
                try:
                    escolha = int(
                        input(f"Sua vez ({COR_X}X{RESET}). Escolha (1-9): "))
                    if choice_invalida(escolha, tabuleiro):
                        print("❌ Posição inválida ou ocupada!")
                        time.sleep(1.5)
                        continue 
                except ValueError:
                    print("❌ Digite apenas números!")
                    time.sleep(1)
                    continue

                pos = escolha - 1
                linha, coluna = pos // 3, pos % 3

            else:
                print(f"Computador ({COR_O}O{RESET}) está pensando...")
                time.sleep(1.5)

                livres = []
                for i in range(3):
                    for j in range(3):
                        if tabuleiro[i][j] not in ["X", "O", COR_X+'X'+RESET, COR_O+'O'+RESET]:
                            livres.append((i, j))

                linha, coluna = random.choice(livres)

            simbolo_visual = COR_X + "X" + RESET if jogador_atual == "X" else COR_O + "O" + RESET

            tabuleiro[linha][coluna] = simbolo_visual
            rodadas += 1

            if verificar_vitoria(tabuleiro, simbolo_visual):
                mostrar_tabuleiro(tabuleiro)
                print(f"🎉 PARABÉNS! O Jogador {simbolo_visual} venceu!")
                jogo_ativo = False

            elif rodadas == 9:
                mostrar_tabuleiro(tabuleiro)
                print("🐢 DEU VELHA! (Empate)")
                jogo_ativo = False

            jogador_atual = "O" if jogador_atual == "X" else "X"

        if input("\nJogar novamente? (s/n): ").lower() != 's':
            print("Até a próxima!")
            break


def choice_invalida(escolha, tab):
    if escolha < 1 or escolha > 9:
        return True

    pos = escolha - 1
    l, c = pos // 3, pos % 3
    conteudo = tab[l][c]
    if "X" in conteudo or "O" in conteudo:
        return True

    return False


if __name__ == "__main__":
    jogar()
