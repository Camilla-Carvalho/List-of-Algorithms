matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]] #cada zero em uma linha indica uma coluna

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite o valor para o índice : [{linha}, {coluna}]: '))

for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end ='')
    print()

