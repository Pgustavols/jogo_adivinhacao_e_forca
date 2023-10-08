import forca
import adivinhação

def escolhe_jogo():

    print("*"*35)
    print("Bem-vindo ao Jogo!")
    print("*"*35)

    print("(1) Forca (2) Adivinhação")
    jogo = int(input("Informe qual jogo você quer jogar: "))

    if(jogo == 1):
        forca.jogar()
    elif(jogo == 2):
        adivinhação.jogar()

if(__name__ == "__main__"):
    escolhe_jogo()
