def jogar_adivinhacao():

    import random as ra

    numero_secreto = ra.randrange(1,101)
    total_de_tentativas = 0
    pontos = 1000

    print ('\nVamos adinhar um número !\n')

    nivel() # Chamando a função nível

    opcao = int(input('\nQual você deseja: '))

    while opcao > 3 or opcao == 0:
       print('\nVocê digitou um dado inválido, digite novamente.\n')
       nivel()
       opcao = int(input('\nQual você deseja: '))

    if (opcao == 1):
        chances = 20
    elif (opcao == 2):
        chances = 10
    elif (opcao ==3):
        chances = 5

    total_de_tentativas= chances

    for rodada in range(1,total_de_tentativas +1):

        tentativa = int(input(f'Rodada {rodada} de {total_de_tentativas}.\n\nAdivinhe um número entre 1 e 100: '))

        if (tentativa < 1 ) or (tentativa > 100):
            print('\nVocê digitou um número fora dos limites. Perdeu uma rodada.')
            continue

        if  (tentativa!= numero_secreto) :
            pontos = pontos - abs(numero_secreto-tentativa)
            if (tentativa > numero_secreto):
                print('Seu chute foi maior que o número secreto.\n')
            elif (tentativa < numero_secreto):
                print('Seu chute foi menor que o número secreto.\n')

        else:
            print(f'\nVocê acertou!\nSeus pontos são: {pontos}')
            break

        if (rodada == chances and tentativa != numero_secreto):
            print(f'O número secreto era {numero_secreto}')

    print('\nFim de jogo.')

def nivel():
        print('''Escolha sua dificuldade:\n\n1 - Fácil\n2 - Médio\n3 - Difícil''')

if (__name__ == '__main__'):
    jogar_adivinhacao()