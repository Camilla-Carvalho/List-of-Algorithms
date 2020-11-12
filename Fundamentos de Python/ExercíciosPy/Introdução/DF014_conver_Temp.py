import time
print('Cnvertendo temperatura de graus Cº em Fº')
C = float(input('Digte a temperatura em graus Cº: '))
F = ((9 * C) / 5) + 32
time.sleep(1)
print('...')
time.sleep(1)
print('Processando...')
time.sleep(4)
print('-'*60)
print(f'A temperatura de {C:.0f}Cº seguindo a conversão, é equivalente a {F}Fº')
