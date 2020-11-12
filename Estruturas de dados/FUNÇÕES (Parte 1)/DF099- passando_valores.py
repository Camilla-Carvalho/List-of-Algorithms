def maior(* var):
    for i, value in var:
        print(i)

lista = [2, 9, 4, 7, 5, 1]
maior(lista)

def listas(validação):
    while True:
        value = int(input('Digite um valor: '))
        lista.append(value)
        option = ' '
        while option not in 'SN':
            option = input('Deseja continuar? [S/N]: ').strip().upper()[0]
            if option not in 'SN':
                print('OPÇÃO INVÁLIDA!', end='')
        if option == 'N':
            break
    print(lista)

# cinco listas
#principal program
lista = []

