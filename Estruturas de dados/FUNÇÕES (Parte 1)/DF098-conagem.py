from time import sleep


def contador(inicio, fim, passo):
    if fim < inicio:
        fim = -fim
    if passo == 0:
        passo = -1
        print(f'Contagem de {inicio} até {fim} de 1 em 1: ')
    else:
        print(f'Contagem de {inicio} até {fim} de {passo} em {passo}: ')
    for i in range(inicio, fim, passo):
        sleep(0.7)
        print(f'{i} ', end='')
        i += 1
    print('FIM.')


def cont():
    print('\nNúmeros de até 10 de um em um: ')
    for i in range(0, 10):
        print(f'{i + 1} ', end='')
        sleep(0.7)
    print()
    print('=-' * 26, '\nNúmeros de 1 até 10 em ordem regressiva de dois em dois: ')
    for i in range(10, 0, -2):
        sleep(0.7)
        print(f'{i} ', end='')
        i += 1
    print()
    print('-=' * 26)

# principal program
cont()

print('Agora é sua vez de personalizar: ')
contador(inicio=int(input('Inicio: ')), fim=int(input('Fim: ')), passo=int(input('Passo: ')))