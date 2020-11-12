i = 0
soma = 0
contador = 0
for i in range(1,7):
    i = int(input(f'Digite o {i} valor: '))
    if i % 2 == 0:
        soma += i
        contador += 1
print(f'Você informou {contador} números pares e a soma de todos é {soma}')

