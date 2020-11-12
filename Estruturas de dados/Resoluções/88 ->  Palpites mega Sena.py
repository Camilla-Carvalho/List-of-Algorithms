def title(txt):
    print('-'*30)
    print('JOGO NA MEGA SENA')
    print('-'*30)

title('')
from random import randint
from time import sleep
lista = []
jogos = []
quantidade = int(input('Digite a quantidade de jogos que deseja sortear: '))
total = 1
while total <= quantidade:
    cont = 0  ##cont deve receber zero dentro do laço.
    while True:
        numero = randint(1, 60)
        if numero not in lista:
            lista.append(numero)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1

print('-=' * 3, f'Sorteando {quantidade} Jogos', '-=' * 3)
for indice, linha in enumerate(jogos):
    print(f'Jogo {indice + 1}: {linha}')
    sleep(1)
