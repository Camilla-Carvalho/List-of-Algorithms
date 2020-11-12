def cabecalho(txt):
    print('\033[36m=-'*15)
    print('PAR OU IMPAR?')
    print('=-' * 15)
def linha(lin):
    print('--'*20)

from random import randint
result = par = impar = soma = cont = 0
cabecalho('')

while True:
    jogador = int(input('\033[0mDigite um valor: '))
    computador = randint(0, 10)
    linha('')
    soma = (jogador + computador)
    option = input('Par ou impar? [P/I]: ').strip().upper()[0]
    linha('')
#validacao de dados
    while option not in 'PI':
        print('\033[31mOPÇAO INVALIDA!\033[0m')
        option = input('Par ou impar? [P/I]: ').strip().upper()[0]
#Condiçao
    if soma % 2 == 0:
        par = soma
    else:
        impar = soma
#Jogador
    if soma == par and option in 'P':
        print(f'Voce jogou {jogador} e computador {computador}. Total de {soma} deu Par.')
        print('\033[34mVOCE VENCEU!\033[0m')
        linha('')
        cont += 1
    elif soma == impar and option in 'I':
        print(f'Voce jogou {jogador} e computador {computador}. Total de {soma} deu Impar.')
        print('\033[34mVOCE VENCEU!\033[0m')
        linha('')
        cont += 1

#computador
    elif soma == par and option in 'I':
        print(f'Voce jogou {jogador} e computador {computador}. Total de {soma} deu Impar.')
        if cont == 0:
            print(f'\33[31m====GAME OVER!====\n Você não acertou porra nenhuma')
            break
        else:
            print(f'\33[31mGAME OVER!\033[34m Você venceu {cont} vezes')
            break
    else:
        print(f'Voce jogou {jogador} e computador {computador}. Total de {soma} deu Impar.')
        if cont == 0:
            print(f'\33[31m=====GAME OVER!=====\n Voce não acertou porra nenhuma...')
            break
        else:
            print(f'\33[31m====GAME OVER!====\n\033[34m Voce venceu {cont} vezes')
            break
        break




