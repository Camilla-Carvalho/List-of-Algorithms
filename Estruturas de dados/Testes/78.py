lista = []
maior = menor = 0
for i in range(0, 5):
    lista.append(int(input(f'Digite um valor para a posição {i}: ')))
    maior = max(lista)
    menor = min(lista)

print(f'O maior valor digitado foi {maior}, nas posições: ', end='')
for indice, i in enumerate(lista):
    if i == maior:
        print(f' {indice}', end='...')
print(f'\nO menor valor digitado foi {menor}, nas posições: ', end='')
for indice, i in enumerate(lista):  #I é o conteúdo, e i indice é a posição do conteúdo.
    if i == menor:
        print(f' {indice}', end='...')






