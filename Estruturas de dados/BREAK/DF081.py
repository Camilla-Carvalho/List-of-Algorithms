lista = list()

while True:
    option = ' '
    num
    while option not in 'SN':
        numero.append(int(input('Digite um número: ')))
        option = input('Deseja continuar?[S/N]: ').strip().upper()[0]
    if option != 'SN':
        print('opção inválida!')
    if option == 'N':
        print('Fim do programa')


