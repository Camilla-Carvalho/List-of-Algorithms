valores = list()

for i in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {i}: ')))
    maior = max(valores)
    menor = min(valores)

print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {maior} na posição {valores.index(maior)}')
print(f'E o menor valor digitado foi {menor} na posição {valores.index(menor)}')


