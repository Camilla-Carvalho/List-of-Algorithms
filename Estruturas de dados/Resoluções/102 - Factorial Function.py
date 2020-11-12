from time import sleep


def factorial(value=1, show=False):
    """
    -> Calcula o fatorial de um número
    :param value:  Valor a ser calculado
    :param show: (opcional) Mostrar ou não processo da conta
    :return: O valor de Factorial de um número n
    """
    f = 1
    for i in range(num, 0, -1):
        f *= i
        if show:
            print(i, end='')
            if i > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
    return f


def verific():
    option = ' '
    while option not in 'SN':
        option = input('Deseja continuar?[S/N]: \033[0m').strip().upper()[0]
        if option not in 'SN':
            print('\033[31mOPÇÃO INVÁLIDA!', end='')
        if option == 'S':
            print(factorial.__doc__)
        else:
            print('Obrigada, volte Sempre!')
        print('-=' * 20)

#principal Program
num = int(input('Type a value: '))
print(factorial(num, show=True))
print('-=' * 20)
verific()

sleep(4)
print('Fim do programa')



