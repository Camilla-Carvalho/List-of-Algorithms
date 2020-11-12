from random import randint
from time import sleep


def sorteia(lista):
    print(f'\nSorteando 5 valores da lista: ', end='')
    for cont in range(0, 5):
        num = randint(1, 10)
        lista.append(num)
        print(f'{num} ', end='', flush=True)
        sleep(0.3)
    print('PRONTO!')


def somaPar(lista):
    soma = 0
    for value in lista:
        if value % 2 == 0:
            soma += value
    print(f'Somado os valores pares de {lista} temos {soma}')

numero = list()
sorteia(numero)
somaPar(numero)
