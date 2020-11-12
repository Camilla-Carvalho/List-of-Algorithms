from random import randint
cont = 1
print('Sou seu computador...\nAcabei de pensar em um número entre 0 e 10...', end='')
print('Será que você consegue adivinhar qual foi?')
jogador = int(input('Digite seu palpite: '))
computador = randint(1, 10)
while computador != jogador:
    if jogador < computador:
        jogador = int(input('Mais... Tente novamente: '))
        cont += 1
    else:
        jogador = int(input('Menos... Tente novamente: '))
        cont += 1
print(f'Parabéns! você acertou depois de {cont} tentatvas!')


