from random import randint
print('Sou seu computador... Pensei em um número de 0 a 10\n Acha que consegue adivinhar? ')
computador = randint(0,10)
palpite = 1
acertou = False
while not acertou:
    palpite += 1
    jogador = int(input('Qual é seu palpite? '))
    if jogador == computador:
        acertou == True
    else:
        if computador < jogador:
            print('Menos... Tente mais uma vez')
        elif computador > jogador:
            print('Mais...Tente mais uma vez. ')
print(f'Você acertou depois de {palpite} tentativas')

