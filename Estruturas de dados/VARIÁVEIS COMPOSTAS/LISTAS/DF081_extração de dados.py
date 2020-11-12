lista = list()
while True:
    lista.append(int(input('Digite um número: ')))
    option = ' '
    while option not in 'SN':
        option = input('Deseja continuar? [S/N]: ').strip().upper()[0]
        if option not in 'SN':
            print('OPÇÂO INVÀLIDA!', end='')
    if option in 'N':
        print('FIM DO PROGRAMA.')
        break
        print('-'*30)
print(f'Você digitou {len(lista)} elementos')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são: {lista}', end='')
if 5 in lista:
    print(f'\nO valor cinco faz parte da lista!')
else:
    print('\nO valor 5 não foi encontrado dentro da lista.')



