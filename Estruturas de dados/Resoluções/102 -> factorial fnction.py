def lin():
    print('-' * 31)

def header(txt):
    print('\n', '=' * len(txt),'\n', txt, '\n', '=' * len(txt))


def function(var=1, show=True):
    f = 1
    for i in range(var, 0, -1):
        f *= i
        if show:
            print(i, end='')
            if i > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
    return f


header(f'{"F A T O R I A L":^30}')
while True:
    num = int(input('Type a value: '))
    lin()
    option = ' '
    while option not in 'SN':
        option = str(input('Deseja ver a operação?[S/N]: \033[0m')).strip().upper()[0]
        lin()
        if option not in 'SN':
            print('\033[31mOPÇÃO INVÁLIDA! ', end='')
        if option in 'S':
            print(function(num, show=True))
            break
        if option == 'N':
            print(function(num, show=False))
            break
    lin()
    option = ' '
    while option not in 'SN':
        option = str(input('Deseja realizar outro calculo?[S/N]: \033[0m')).strip().upper()[0]
        if option not in 'SN':
            print('\033[31mOPÇÃO INVÁLIDA!', end='')
    while option == 'S':
        print('''
     [ 1 ] SOMA
     [ 2 ] MULTIPLICAÇÃO
     [ 3 ] DIVISÃO
     [ 4 ] SUBTRAÇÃO\n''')
        option = int(input('Digite uma opção: '))
        if option == 1:
            n1 = int(input('Digite um valor para ser somado: '))
            n2 = int(input('Digite outro valor para ser somado: '))
            print(f'A soma de {n1} + {n2} = {n1 + n2}')
            break
        elif option == 2:
            n1 = int(input('Digite um valor para ser multiplicado: '))
            n2 = int(input('Digite outro valor para ser multiplicado: '))
            print(f'A multiplicação entre {n1} x {n2} = {n1 * n2}')
            break
        elif option == 3:
            n1 = int(input('Digite um valor para ser dividido: '))
            n2 = int(input('Digite outro valor para ser dividido: '))
            print(f'A divisão entre {n1} / {n2} = {n1 / n2}')
        elif option == 4:
            n1 = int(input('Digite um valor para ser substraído: '))
            n2 = int(input('Digite outro valor para ser subtraído: '))
            print(f'A subtração entre {n1} - {n2} = {n1 - n2}')
            break
    if option == 'N':
        break
    lin()
    print('Obrigada por usar nosso programa. Volte sempre!')





