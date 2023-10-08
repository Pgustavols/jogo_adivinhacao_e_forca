import random

def jogar():
    numero_aleatorio = random.randrange(1, 101)
    total_de_rodada = 0
    rodada = 1
    pontos = 1000

    print("Qual nível de dificuldade? ")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina um nível: "))

    if(nivel == 1 or nivel == 2 or nivel == 3):

        if(nivel == 1):
            total_de_rodada = 10

        elif(nivel == 2):
            total_de_rodada = 5

        else:
            total_de_rodada = 3

    else:
        print("É preciso digitar um número entre 1 e 3.")

    for rodada in range(1, total_de_rodada + 1):
        print("*"*35)
        chute = int(input("Insira um número entre 1 e 100: "))

        print("Rodada {} de {}".format(rodada, total_de_rodada))

        acertou = chute == numero_aleatorio
        maior = chute > numero_aleatorio
        menor = chute < numero_aleatorio

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número inteiro entre 1 e 100.")
            continue

        if(acertou):
            pontos += 600
            print("Parábens! Você acertou o número sorteado e fez {} pontos!".format(pontos))
            break

        else:
            if(maior):
                print("O número que você digitou é MAIOR que o número sorteado.")

            elif(menor):
                print("O número que você digitou é MENOR que o número sorteado.")

        pontos_perdidos = abs(numero_aleatorio - chute)
        pontos = pontos - pontos_perdidos


    if(rodada == total_de_rodada and chute != numero_aleatorio):
        print("O número sorteado foi {}".format(numero_aleatorio))


    print("Fim de Jogo!")
    print("*" * 35)

if(__name__ == "__main__"):
    jogar()