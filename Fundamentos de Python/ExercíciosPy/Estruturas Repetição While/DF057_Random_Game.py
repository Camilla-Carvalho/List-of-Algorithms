from random import randint
print('Sou seu computador...\nAcabei de pensar em número entre 0 e 10.\nSerá que consegue adivinhar qual foi?')
jogador = int(input('Qual é seu palpite? '))
computador = randint(0, 10)
cont = 1
while jogador != computador:
    cont += 1
    if computador > jogador:
        jogador = int(input('Mais... Qual seu palpite? '))
    else:
        jogador = int(input('Menos... Qual seu palpite? '))
print(f'Você acertou com {cont} tentativas, Parabéns!')


