
lista = [[],[]]
for i in range(0, 7):
    valor = int(input(f'Digite o {i + 1}º valor: '))
    if valor % 2 == 0:
        lista[0].append(valor)
        lista[0].sort()
    else:
        lista[1].append(valor)
        lista[1].sort()

print(f'Os valores pares foram: {lista[0]}\nOs valores ímpares foram: {lista[1]}')