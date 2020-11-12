def linha(lin):
    print('-' * 45)

lista = []

while True:
    valor = int(input('Digite um valor: '))
    linha('')
    if valor not in lista:
        print(f'\033[34mO número {valor} foi adicionado com sucesso...\033[0m')
        linha('')
        lista.append(valor)
    else:
        print('\033[31mValor duplicado! Não vou adicionar...\033[0m')
        linha('')

    option = ' '
    while option not in 'SN':
        option = input('Deseja continuar?[S/N]: \033[0m').strip().upper()[0]
        if option not in 'SN':
            print('\033[31mOPÇÃO INVÁLIDA! ', end='')

    linha('')
    if option in 'N':
        break
