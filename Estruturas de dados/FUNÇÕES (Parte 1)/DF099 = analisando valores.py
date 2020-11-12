from time import sleep

def lin():
    print('-=' * 20)


def maior(* var):
    cont = maior = 0
    lin()
    print('Analisando os valores passados...')
    for valor in var:
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                    maior = valor
        cont += 1
    print(f'\nForam informado {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}')

# principal program
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()