def apresentação(txt):
    print('=' * 40)
    print(f'{"L O C A D O R A":^40}')
    print('=' * 40)


locadora = []
filme = {}
apresentação('')
while True:
    filme['titulo'] = input('Digite o nome do filme: ')
    filme['ano'] = int(input('Digite o ano: '))
    filme['diretor'] = input('Digite nome do diretor: ')
    locadora.append(filme)
    option = ' '
    while option not in 'SN':
        option = ('Deseja continuar?[S/N]: ').strip().upper()[0]
        if option not in 'SN':
            print('OPÇÂO INVÀLIDA!', end=' ')
    if option in 'N':
        break

