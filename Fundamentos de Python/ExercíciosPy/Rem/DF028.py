from random import randint
from time import sleep
print('Escolhereiu número de 0 a 5, tene aivinhar...')
x = 0
while(x != -1):
    jogador = int(input('\033[34mDigite um número de 0 a 5: \033[34m'))
    print('=-'*20)
    computador = randint(0,5)
    print('\033[0mProcessando...')
    sleep(3)
    print(f'O número escolhido foi: \n \033[35m====== {computador} =======')

if computador == jogador:
    print('\033[34mPARAÉNS!! Você acertou :\033[0m)')
    print('=' * 35)
else:
    print('\033[31mNão foi dessa vez...\033[0m]')
    print('=' * 35)



