import random

def jogar_focar():

    mensagem_abertura()
    palavra_secreta = palavras_secretas()
    letras_acertadas = inicializa_letras_acertadas (palavra_secreta)

    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0
    tentativas = 7

    # Enquanto not false (true) and not false(true):
    while (not acertou and not enforcou):
        print(f'\nVocê ainda possui {tentativas} tentativas')

        tentativa_letra = pede_chute()

        if (tentativa_letra == ''):
            print('\nVocê não digitou nenhuma letra.')
            continue
        print('')
        if (tentativa_letra in palavra_secreta):

            chute_correto(tentativa_letra,palavra_secreta,letras_acertadas)

        else:
            erros = erros + 1
            tentativas = tentativas - 1
            desenho_forca(erros)

        print(letras_acertadas)

        enforcou = erros == 7  # Quando erros chegar a 6 ele vai ficar False mudando o atributo do enforcou.
        acertou = '_' not in letras_acertadas # Quando não tiver mais o '_' ele vai virar False.

    if (acertou):
        mensagem_vencedor()
    else:
        mensagem_perdedor(palavra_secreta)

def mensagem_abertura():
    print ('\nVamos brincar de forca !\n')

def palavras_secretas():
    with open ('palavras.txt','r') as arquivo:
        palavras = []
        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)

        numero = random.randrange(0,len(palavras))

        palavra_secreta = palavras[numero].upper()
        return palavra_secreta
        #quantidade = len(palavra_secreta)
        #letras_acertadas = ['_'] * quantidade
        #Pode ser feito com essas linhsa, ou usando list comprehensions

def inicializa_letras_acertadas (palavra_secreta):
    return ['_' for letras in palavra_secreta] # Isso é o list comprehensions

def pede_chute():
    tentativa_letra = str(input('\nEscreva uma letra: '))
    tentativa_letra = tentativa_letra.strip().upper()
    return tentativa_letra

def chute_correto(tentativa_letra, palavra_secreta, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if (tentativa_letra in letra):
            letras_acertadas[index] = letra
        index = index + 1

def mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print(f"A palavra era {palavra_secreta}")
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def desenho_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if (erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if (erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if (erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if (erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if (erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if (erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if (__name__ == '__main__'):
    jogar_focar()