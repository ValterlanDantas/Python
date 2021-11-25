import os
from random import randint
opcoes = ["Pedra", "Papel", "Tesoura"]


def jogadas():
    print("""1 - Pedra
2 - Papel
3 - Tesoura""")


while True:
    os.system("cls")
    jogadas()
    try:
        jogada = int(input("Escolha sua jogada: "))
        if 0 < jogada < 4:
            pc = randint(1, 3)
        else:
            print("\njogada invalida\n")
            continue
    except:
        print("\njogada invalida\n")
    else:
        print(f"\nVoce = {opcoes[jogada-1]}\nPC = {opcoes[pc-1]}\n")
        if jogada == pc:
            print("Empate!!!")
        elif jogada == 1 and pc == 3:
            print("Voce Ganhou!!!")
        elif jogada == 2 and pc == 1:
            print("Voce Ganhou!!!")
        elif jogada == 3 and pc == 2:
            print("Voce Ganhou!!!")
        else:
            print("Voce Perdeu!!!")
    os.system("pause")
