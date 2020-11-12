from random import randint
from time import sleep
jogador = {}
lista = list()
time = list()
soma = 0
while True:
    jogador.clear()
    jogador['nome'] = input('Nome do jogador: ').capitalize()
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    lista.clear()
    sleep(1)
    for i in range(0, partidas):
        gol = randint(0, 5)
        print(f'Quantos gols na partida {i+1}? {gol}')
        lista.append(gol)
        soma += gol
        time.append(jogador.copy())
    jogador['gols'] = lista
    jogador['total'] = soma
    while True:
        option = input('Deseja continuar?[S/N]: ').strip().upper()[0]
        if option in 'SN':
            break
        print('OPÇÃO INVÀLIDA!', end=' ')
    if option in 'N':
        break
print('-' * 40)
for key, value in enumerate(time):
    print(f'{key:>3}', end='')
    for dado in value.values():
        print(f'{str(dado):<15}', end='')
        print()

print('-'*40)