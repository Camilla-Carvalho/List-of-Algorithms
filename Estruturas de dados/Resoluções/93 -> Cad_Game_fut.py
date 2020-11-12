from random import randint
from time import sleep
jogador = {}
lista = []
jogador['nome'] = input('Nome: ')
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for i in range(0, partidas):
    gol = randint(0, 6)
    print(f'Quantos gols na partida {i+1}? {gol}')
    lista.append(gol)
    sleep(1)
jogador['gols'] = lista
jogador['total'] = sum(lista)
print('-='*30)
print(jogador)
print('-='*30)
sleep(1)
for key, value in jogador.items():
    print(f'O campo {key} tem valor {value}')
print('-='*30)
sleep(1)
print(f'O jogador {jogador["nome"]} jogou {jogador["total"]} partidas.')
for i, value in enumerate(lista):
    print(f'Na partida {i}, fez {value} gols')
print(f'Foi um total de {jogador["total"]} gols.')



