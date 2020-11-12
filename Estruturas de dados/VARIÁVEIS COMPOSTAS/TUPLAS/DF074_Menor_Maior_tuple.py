from random import randint
numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10)) #Ao colocarmos parenteses a variável vira uma tupla.

print('Os valores sorteados foram: ', end='')

for i in numeros:
    print(f'{i}', end=' ')

print(f'\n\nO maior valor sorteado foi {max(numeros)}\nO menor {min(numeros)}') #Específicos de tuplas -> para ver o maior valor
