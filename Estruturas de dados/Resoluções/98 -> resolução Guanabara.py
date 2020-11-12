from time import sleep


def contador(i, f, p):
    if p == 0:
        p = -1
    print(f' Contagem de {i} até {f} contando de {p} e {p}')
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont += p
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont -= p
    print('Fim')


contador(1, 10, 1)
contador(10, 0, 2)
contador(i=int(input('Início: ')), f=int(input('Fim: ')), p=int(input('Passo: ')))

