dados = list()
pessoas = []
while True:
    nome = input('\033[0mDigite um nome: ')
    peso = float(input('Digite o peso: '))
    dados.append(nome)
    dados.append(peso)
    pessoas.append(dados[:])
    option = ' '
    while option not in 'SN':
        option = input('Deseja continuar?[S/N]: ').strip().upper()[0]
        if option not in'SN':
            print('\033[31mOPÇÂO INVÁLIDA!', end='')
    if option == 'N':
        print('{}'.format('FIM DO PROGRAMA'))
        break
print(pessoas)