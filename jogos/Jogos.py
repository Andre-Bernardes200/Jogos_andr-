import forca
import adivinhacao

def escolha_jogo ():
    print ('''\nEscolha um jogo:\n1 - Forca\n2 - Adivinhação''')
    jogo = int(input('Qual você vai jogar: '))

    if (jogo ==1):
        print('Abrindo Forca')
        forca.jogar_focar()

    elif(jogo==2):
        print('\nAbrindo Adivinhação')
        adivinhacao.jogar_adivinhacao()

if (__name__ == '__main__'):
    escolha_jogo()