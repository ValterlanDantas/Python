import os

jogador = 1
jogadores = ["Telan", "Val"]

mapa = [
    ["7", "8", "9"],
    ["4", "5", "6"],
    ["1", "2", "3"]
]

while True:
    pontos1 = 0
    pontos0 = 0
    os.system("cls")
    print(f"\n\
{mapa[0][0]} | {mapa[0][1]} | {mapa[0][2]}\n\
_________\n\
{mapa[1][0]} | {mapa[1][1]} | {mapa[1][2]}\n\
_________\n\
{mapa[2][0]} | {mapa[2][1]} | {mapa[2][2]}\n\
            ")
    posicao = 0
    try:
        jogada = int(input(f"jogue {jogadores[jogador]}: ")) - 1
        if jogada < 0 or jogada > 9:
            print("jogada invalida")
            continue
    except:
        print("jogada invalida")
    else:
        errada = "n"
        for i in range(3):
            if errada == "s":
                break
            else:
                pontos = 0
                for x in range(3):
                    if posicao == jogada:
                        if mapa[i][x] == "X" or mapa[i][x] == "0":
                            errada = "s"
                            print("jogada invalida")
                            os.system("pause")
                            break
                        if jogador == 1:
                            mapa[i][x] = "X"
                            jogador = 0
                        else:
                            mapa[i][x] = "0"
                            jogador = 1
                    if mapa[i][x] == "X":
                        pontos += 1
                        if pontos == 3:
                            print(f"jogador {jogadores[1]} ganhou")
                            os.system("pause")
                    if mapa[i][x] == "0":
                        pontos += 1
                        if pontos == 3:
                            print(f"jogador {jogadores[0]} ganhou")
                            os.system("pause")
                    if jogador == 0:
                        if mapa[x][i] == "0":
                            pontos0 += 1
                            if pontos0 == 3:
                                print(f"jogador {jogadores[1]} ganhou")
                                os.system("pause")
                    if jogador == 1:
                        if mapa[x][i] == "X":
                            pontos1 += 1
                            if pontos1 == 3:
                                print(f"jogador {jogadores[0]} ganhou")
                                os.system("pause")
                    posicao += 1
