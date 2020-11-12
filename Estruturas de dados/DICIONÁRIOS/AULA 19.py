filmes = {}
while True:
    filmes['filme'] = input('Digite o nome do filme: ')
    filmes['ano'] =int(input('Digite ano: '))
    filmes['diretor'] = input('Digite nome do diretor: ')
    option = ' '
    while option not in 'SN':
        option = input('Deseja continuar?[S/N]: ').strip().upper()[0]
        if option not in 'SN':
            print('OPÇÃO INVÀLIDA!', end=' ')
    if option in 'N':
        break
print(filmes.values())
print(filmes.keys())
print('-'*30)
print(filmes.items())



