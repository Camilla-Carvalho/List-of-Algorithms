from random import randint
cont = 1
print('Sou seu computador...\nAcabei de pensar em um número entre 0 e 10!\nAcha que consegue adivinhar?')
jogador = int(input('Digite seu palpite: '))
computador = randint(0, 10)
while jogador != computador:
    if jogador < computador:
        cont += 1
        jogador = int(input('Um pouco mais... Tente novamente: '))
    elif jogador > computador:
        cont += 1
        jogador = int(input('Um pouco menos... Tente novamente: '))
    else:
        print('Parabéns!')
print(f'Você acertou depois de {cont} tentativas!')



