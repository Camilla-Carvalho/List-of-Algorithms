lista = []

for i in range(0, 5):
    numero = int(input('Digite um número: '))
    if i == 0 or numero < lista[-1]:
        lista.append(numero)
        print('Adicionado ao final da lista...')
    else:
        posição = 0
        while posição < len(lista): #número de índices da lista.
            if numero <= lista[posição]:
                lista.insert(posição, numero)
                print(f'Adicionado na posição {posição} da lista...')
                break
                posição += 1
print('-'*30)
print(f'Os valores digitados foram {lista}')


# if i == 0:
#     lista.append(i)
# elif numero > lista[len(lista)-1]: #Para pegar o último elemento da lista == lista[-1] \\ Maior que o ultimo elemento
#     lista.append(i)
