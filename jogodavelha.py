def imprimir_tabuleiro(tabuleiro):
    print("-------------")
    for i in range(3):
        print("|", end=" ")
        for j in range(3):
            print(tabuleiro[i][j], "|", end=" ")
        print("\n-------------")

def verificar_vencedor(tabuleiro):
    for i in range(3):
        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] != " ":
            return True

    for i in range(3):
        if tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] != " ":
            return True

    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] != " ":
        return True
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] != " ":
        return True

    return False

def jogar_jogo_da_velha():
    tabuleiro = [[" ", " ", " "],
                 [" ", " ", " "],
                 [" ", " ", " "]]

    jogador = "X"

    while True:
        imprimir_tabuleiro(tabuleiro)

        linha = int(input("Digite o número da linha (0, 1 ou 2): "))
        coluna = int(input("Digite o número da coluna (0, 1 ou 2): "))

        if tabuleiro[linha][coluna] == " ":
            tabuleiro[linha][coluna] = jogador
        else:
            print("Posição inválida. Tente novamente.")
            continue

        if verificar_vencedor(tabuleiro):
            imprimir_tabuleiro(tabuleiro)
            print("Jogador", jogador, "ganhou!")
            break

        if jogador == "X":
            jogador = "O"
        else:
            jogador = "X"

jogar_jogo_da_velha()
