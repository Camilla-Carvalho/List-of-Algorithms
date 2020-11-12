from time import sleep


def lin():
    print('-=' * 20)


def maior(* var):
    lin()
    cont = maior = 0
    print('Analyzing past values...')
    for value in var:
        print(f'{value} ', end='', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = value
        else:
            if value > maior:
                maior = value
        cont += 1
    print(f'\nForam informados {cont} valores\nO maior valor informado foi {maior}')


#principal program
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()