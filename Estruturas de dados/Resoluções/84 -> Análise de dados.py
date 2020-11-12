dados_temporários = []
lista_principal = []
maior = menor = 0
while True:
    dados_temporários.append(input('\033[0mNome: ').capitalize())
    dados_temporários.append(float(input('Peso: ')))

    if len(lista_principal) == 0:  ##len de principal.
        maior = menor = dados_temporários[1]
    else:
        if dados_temporários[1] > maior:
            maior = dados_temporários[1]
        if dados_temporários[1] < menor:
            menor = dados_temporários[1]

    lista_principal.append(dados_temporários[:])
    dados_temporários.clear() ## --> limpamos para não replicar os dados na próx lista.
    option = ' '
    while option not in 'SN':
        option = input('Deseja continuar?[S/N]: ').strip().upper()[0]
        if option not in 'SN':
            print('\033[31mOPÇÂO INVÁLIDA! ',end='')
    if option == 'N':
        print('FIM DO PROGRAMA!')
        break

print(f'{len(lista_principal)} pessoas foram cadastradas')
print(f'O maior peso foi de: {maior}kg', end=' ')
for pessoa in lista_principal:
    if pessoa[1] == maior:
        print(f'[{pessoa[0]}]', end=' ')
print(f'\nO menor peso foi de: {menor}kg:', end=' ')
for pessoa in lista_principal:
    if pessoa[1] == menor:
        print(f'[{pessoa[0]}]', end=' ')