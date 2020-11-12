def cabecalho(txt):
    print('='*30)
    print('MENU COM OPÇÕES')
    print('=' * 30)

def linha(lin):
    print('~' * 30)



linha('')
primeiro_numero = int(input('Digite um número: '))
segundo_numero = int(input('Digite outro número: '))
cabecalho('')
option = 0
maior = 0
while option != 5:
    print('''[ 1 ] SOMAR
[ 2 ] MULTIPLCAR
[ 3 ] MAIOR
[ 4 ] NOVOS NÚMEROS
[ 5 ] SAIR 
''')
    option = int(input('Digite uma opção: '))

    if option == 1:
        linha('')
        print(f'A soma de {primeiro_numero} + {segundo_numero} é {primeiro_numero + segundo_numero}')
        linha('')
    elif option == 2:
        linha('')
        print(f'A multiplicação entre {primeiro_numero} x {segundo_numero} = {primeiro_numero * segundo_numero}')
        linha('')
    elif option == 3:
        if primeiro_numero > segundo_numero:
            linha('')
            print(f'O maior número digitado foi {primeiro_numero}')
            linha('')
        else:
            linha('')
            print(f'O maior número digitado foi {segundo_numero}')
            linha('')
    elif option == 4:
        linha('')
        primeiro_numero = int(input('Digite um número: '))
        segundo_numero = int(input('Digite outro número: '))
        linha('')
    elif option == 5:
        print('\033[34mFim do programa!')
    else:
        print('\033[31mOPÇÃO INVÁLIDA')



