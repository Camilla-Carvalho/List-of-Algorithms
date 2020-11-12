from random import randint

valores = list() #Lista vazia
# valores.append(randint(0, 9))
# valores.append(randint(0, 9))
# valores.append(randint(0, 9))
# valores.append(randint(0, 9))

for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

valores.sort(reverse=True)

#for i in valores:
for keys, i in enumerate(valores):
 print(f'Na posição {keys} encontrei o valor {i}')
print('Chegei ao final da lista...')
