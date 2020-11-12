dados = []
lista_principal =  []
maior = menor = 0
while True:
    dados.append(input('Nome: ').capitalize())
    dados.append(float(input('Peso: ')))

    if len(lista_principal) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] < menor:
            menor = dados[1]
        if dados[1] > maior:
            maior = dados[1]

    lista_principal.append(dados[:])
    dados.clear() ##Colocar .clear sempre que fizer umacomparação, para não acumular valores em outras listas.
    option = ' '
    while option not in 'SN':
        option = input('Deseja continuar?[S/N]: ').strip().upper()[0]
        if option not in 'SN':
            print('OPÇÃO INVÁLIDA!', end=' ')
    if option == 'N':
        print('\n====FIM DO PROGRAMA====')
        break

print(f'O maior peso foi de {maior}kg. Peso de ', end='')
for pessoa in lista_principal:
    if pessoa[1] == maior:
        print(f'[{pessoa[0]}] ', end='')
print(f'\nO menor peso foi de {menor}kg. Peso de ', end='')
for pessoa in lista_principal:
    if pessoa[1] == menor:
        print(f'[{pessoa[0]}] ', end='')
