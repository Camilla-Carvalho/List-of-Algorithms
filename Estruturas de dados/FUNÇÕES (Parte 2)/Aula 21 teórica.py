# print('Olá mundo')
# help(print)


def contador(* var):
    """

    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: none return
    função criada por Camilla Carvalho do CeV
    """
    soma = 0
    for i in var:
        soma += i
    print(soma)


# principal program
contador(2, 4, 6, 7)
contador(2, 1, 1)

option = ' '
while True:
    option = input('Deseja ver a documentação?[S/N]: ').strip().upper()[0]
    if option == 'S':
        print(contador.__doc__)
        break
    elif option in 'N':
        break

