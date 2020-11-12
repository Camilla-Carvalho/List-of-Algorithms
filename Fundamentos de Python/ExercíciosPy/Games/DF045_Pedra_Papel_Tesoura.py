from random import randint
from time import sleep
x = True
while(x == True):
    itens = ('Pedra', 'Papel', 'Tesoura')
    computador = randint(0, 2)
    print('\n\033[35m{:=^40}'.format('PEDRA_PAPEL_TESOURA'))
    print('''\n\033[0mOPÇÕES
    [ 0 ] Pedra
    [ 1 ] Papel
    [ 2 ] Tesoura''')
    jogador = int(input('\nDigite uma opção: '))
    sleep(1)
    print('\nJO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO')
    print('\033[35m=-\033[0m'*15)
    print(f'você jogou: {itens[jogador]}\nComputador jogou: {itens[computador]}')
    print('\033[35m=-'*15)
    if computador == 0:
        if jogador == 0:
            x = False
            print('\033[32mEMPATE')
        elif jogador == 1:
            print('\033[34mVocê VENCEU!')
        elif jogador == 2:
            print('\033[31mVocê PERDEU!')
        else:
            print('OPCÃO INVÀLIDA')
    elif computador == 1:
       if jogador == 0:
           print('\033[31mVocê PERDEU!')
       elif jogador == 1:
           x = False
           print('\033[32mEMPATE')
       elif jogador == 2:
           print('\033[34mVocê VENCEU!')
    elif computador == 2:
        if jogador == 0:
            print('\033[34mVocê GANHOU!')
        elif jogador == 1:
            print('\033[31mVocê PERDEU!')
        elif jogador == 2:
            x = False
            print('\033[32mEMPATE')
        else:
            print('\033[31mOPCÃO INVÀLIDA')
print('Parabéns!')

