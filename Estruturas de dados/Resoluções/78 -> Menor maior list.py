lista = list()
maior = menor = 0
for i in range(0, 5):
    lista.append(int(input(f'Digite um valor na posição {i}: ')))
    if i == 0:
        maior = menor = lista[i] ##Número da lista na posição i
    else:
        if lista[i] > maior:
            maior = lista[i]
        if lista[i] < menor:  ##i indica a posição
            menor = lista[i]
print(f'Você digitou os valores {lista}', end=' ')
print(f'\nO maior valor foi: {maior} nas posições:', end='')
for posição, i in enumerate(lista):
    if i == maior:
        print(f' {posição}...', end='')
print(f'\nO menor valor foi: {menor} nas posições: ', end='')
for posição, i in enumerate(lista):
    if i == menor:
        print(f'{posição}...', end=' ')