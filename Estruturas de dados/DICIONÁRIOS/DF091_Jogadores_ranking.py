def header(txt):
    print('-=' * 15)
    print(f'{"R E S U L T A D O":^30}')
    print('-=' * 15)

from random import randint
from time import sleep
from operator import itemgetter

jogo = {'Jogador1': randint(1, 6),
        'Jogador2': randint(1, 6),
        'Jogador3': randint(1, 6),
        'Jogador4': randint(1, 6)}
ranking = list()
for key, value in jogo.items():
    print(f'O {key} tirou {value}')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
header('')
for i, value in enumerate(ranking):
    print(f'{i + 1}º lugar: {value[0]} {value[1]}')
    sleep(1)

