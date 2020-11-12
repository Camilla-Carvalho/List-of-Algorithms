lista = list()
pares = list()
impares = list()

while True:
    lista.append(int(input('Digite um número: ')))
    resposta = input('Deseja continuar?[S/N]: ')
    if resposta in 'Nn':
        break
for i, valor in enumerate(lista):
    if valor % 2 == 0:
        pares.append(valor)
    elif valor % 2 == 1:
        impares.append(valor)
print('-='*30)
print(f'A lista completa é {lista}\nA lista de pares é {pares}\nA lista de impares é {impares}')