def cabecalho(tit):
    print('='*30)
    print('CÁLCULO DO FATORIAL')
    print('='*30)


cabecalho('')
fat = 1
termo = int(input('Digite o número que deseja fatorar: '))
cont = termo
while cont > 0:
    print(f'{cont}', end='')
    print(' x 'if cont > 1 else ' = ', end='')
    fat *= cont
    cont -= 1
print(fat)

