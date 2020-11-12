valores = []

while True:
    numero = int(input('\033[0mDigite um valor: '))
    if numero not in valores: #Se os números não estiverem nos valores, são adicionados a lista!
        valores.append(numero)
        print('\033[34mValor adicionado com sucesso!...\033[0m')
    else:
        print('\033[31mFALHA AO ADICIONAR! Valor duplicado...\033[0m')
    option = ' '
    while option not in 'SN':
        option = input('Deseja continuar? [S/N]: ').strip().upper()[0]
        if option not in 'SsNn':  ## Not in --- não usar !=
            print('\033[31mOPÇÃO INVÁLIDA! ', end='')

    if option == 'N':
        print('FIM DO PROGRAMA')
        break

print(f'Você digitou os valores: {valores}')
print(f'Lista em ordem crescente: {sorted(valores)}') ##valores.sort()
print(f'Lista em ordem decrescente: {valores.sort(reverse=True)}')

