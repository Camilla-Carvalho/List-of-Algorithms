
from random import randint
from time import sleep
print('\033[35m Pense em um número de 0 a 5... ')
print('-'*30)
x = 0
while (x != -1):
    jogador = int(input('\033[0m Digite esse número: '))
    print('Processando..')
    sleep(3)
    print('\033[35m -='*20)
    computador = randint(0,5)
    print(f'\033[0m O número sorteado foi...\n ====== {computador} ======')
    if jogador == computador:
        print(f'\033[34m O número escolhido foi: {computador}\n Você acertou :)')
    else:
        print(f'\33[31m O número esclhido foi: {computador}\n Você perdeu :(')



