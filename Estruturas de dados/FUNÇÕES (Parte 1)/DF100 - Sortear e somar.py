from random import randint


def teste(list):
    print(f'Sorteando {len(list)} da lista: ', end='')
    for i, value in enumerate(list):
        print(f'{value} ', end='')
    print('PRONTO!')

def teste2(list2):
    cont = 0
    print(f'Somando os valores pares de {list2}, temos: ', end='')
    for i, value in enumerate(list2):
        if value % 2 == 0:
            cont += value
    print(f'{cont}')


lista = [randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9)]
cont = 0
teste(lista)
teste2(lista)

