from time import sleep


def lin():
    print('-=' * 20)


def contador(i, f, p):
    if p < 0:
        p *= -1  # inversão de sinais
    if p == 0:
        p = 1
    lin()
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(1.5)

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= p
        print('FIM!')
        lin()

contador(1, 10, 1)
contador(10, 0, 2)

print('Agora e sua vez de personalizar a contagem! ')
contador(i=int(input('Início: ')), f=int(input('Fim: ')), p=int(input('Passo: ')))
