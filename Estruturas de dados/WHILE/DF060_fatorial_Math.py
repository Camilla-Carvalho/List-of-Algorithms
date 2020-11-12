from time import sleep
print('======CALCULO FATORIAL=======')
num = int(input('Digite um número que deseja calcular do fatorial: '))
cont = num
fat = 1 #Começa com um pelo valor nulo de multiplicação ser 1
print(f'\nCalculando {num}!')
sleep(0.5)
print('Processando...\n')
sleep(2)
while cont > 0:
    print(f'{cont}', end='')
    print(' x 'if cont > 1 else ' = ', end='');
    fat *= cont
    cont -= 1
print(f'{fat}')


