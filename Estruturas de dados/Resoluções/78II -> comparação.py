lista = list()
maior = menor = 0

for i in range(0, 5):
    lista.append(int(input('Digite um número: ')))
    if i == 0:       #Indicar o index // #posição zero
        maior = menor = lista[i]
    else:
        if lista[i] > maior:
            maior = lista[i]
        if lista[i] < menor:
            menor = lista[i]

print(f'Você digitou os valores: {lista}')

print(f'O maior valor digitado foi {maior} nas posições: ', end='')
for posição, i in enumerate(lista):
    if i == maior:
        print(f'{posição}...', end='')

print(f'\nO menor valor digitado foi {menor} nas posições: ', end='')
for posição, i in enumerate(lista):
    if i == menor:
        print(f'{posição}...', end='')