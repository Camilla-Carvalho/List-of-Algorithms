def cabeçalho(lin):
    print('='*40)
    print(f'{"LISTAGEM DE PREÇOS":^40}')
    print('='*40)

cabeçalho('')

produtos = ('Macarrão', 2.99,
            'Molho de tomate', 1.98,
            'Queijo ralado', 1.54,
            'lentilha', 5.98,
            'Leite', 2,
            'Achocolatado', 4.98,
            'Leite de cabra', 8.90,
            'Manteiga', 4.20)

for i in range(0, len(produtos)):
    if i % 2 == 0: #Conta para o número do índice.
        print(f'{produtos[i]:.<32}', end='')
    else:
        print(f'R$ {produtos[i]:.2f}')
print('-'*40)