
from random import randint
from time import sleep
lista = []
jogos = []
option = int(input('Digite a quantidade de jogos que deseja jogar: '))
total = 0
while total <= option:
    cont = 0
    while True:
        numero = randint(1, 60)
        if numero not in lista:
            lista.append(numero)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:]) ## Ficar atenta quanto a identação
    lista.clear()
    total += 1

print('-=' * 3, f'SORTEANDO {option} JOGOS', '-=' * 3)
for indice, linha in enumerate(jogos):
    print(f'Jogo {indice + 1}: {linha}')



