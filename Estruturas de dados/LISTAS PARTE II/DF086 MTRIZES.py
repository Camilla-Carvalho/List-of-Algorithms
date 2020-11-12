matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

#For de alimentação dos valores da matriz
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para a posição para [{linha}],[{coluna}]: '))
print('-='*30)
# Estrutura de repetição para exibir o resultado na tela
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end=' ')
    print() #Para quebra de linha
    #Ao terminar a coluna, o print vazio causa uma quebra de linha.