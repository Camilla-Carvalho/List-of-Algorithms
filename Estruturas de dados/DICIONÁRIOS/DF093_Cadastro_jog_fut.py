from random import randint
from time import sleep
jogador = {}
lista = list()
soma = 0

jogador['nome'] = input('Nome do jogador: ')
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for i in range(0, partidas):
    gol = randint(0, 5)
    print(f'Quantos gols na partida {i+1}? {gol}')
    sleep(1)
    lista.append(gol)
    soma += gol
print('-=' * 30)
jogador['gols'] = lista
jogador['total'] = soma
print(jogador)
print('-=' * 30)
for key, value in jogador.items():
    print(f'O campo {key} tem o valor {value}')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas')
for i, value in enumerate(jogador['gols']):
    print(f'   => Na partida {i}, fez {value} gols.')
print(f'Foi um total de {jogador["total"]}')


