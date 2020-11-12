lista = []
lista_pares = []
lista_impares = []
while True:
    numero = int(input('Digite um número: '))
    lista.append(numero)
    option = ' '
    while option not in 'SN':
        option = input('Deseja continuar?[S/N]: ').strip().upper()[0]
        if option not in 'SN':
            print('OPÇÃO INVÁLIDA!', end='')
    if numero % 2 == 0:
        lista_pares.append(numero)
    else:
        lista_impares.append(numero)
    if option in 'N':
        print('FIM DO PROGRAMA!')
        break
print(f'A lista completa é {lista}')
print(f'A lista de números pares é {lista_pares}')
print(f'A lista de números ímpares é: {lista_impares}')
