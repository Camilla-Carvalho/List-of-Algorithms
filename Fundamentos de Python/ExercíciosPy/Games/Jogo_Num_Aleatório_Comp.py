from random import randint
i = 0
while (i != -1):
    jogador = int(input('\nDigite um número: '))
    print('-='*12)
    computador = randint(0, 5)

    if jogador == computador:
        print('Você ACERTOU!')
    else:
        print(f'O número ecolhido foi {computador} não {jogador}... Você PERDEU!')