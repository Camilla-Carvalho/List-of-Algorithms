def cabeçalho(lin):
    print('-'*40)
    print(f'{"LISTAGEM DE PREÇOS":^40}')
    print('-' * 40)

produtos = ('Lápis', 1.75,
            'Borracha', 2.00,
            'Caderno', 15.90,
            'Estojo', 25.00,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.00,
            'Canetas', 2.30,
            'Livro', 34.20)
cabeçalho('')
for i in range(0, len(produtos)):
    if i % 2 == 0:              ## O índice está na posição par.
        print(f'{produtos[i]:.<30}',end='')
    else:
        print(f'R$ {produtos[i]:.2f}')