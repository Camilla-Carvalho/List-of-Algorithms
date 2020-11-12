from time import sleep

def valid(txt):
    while True:
        if 'sexo' in txt:
            sexo = ' '
            while sexo not in 'FM':
                sexo = input(txt).strip().upper()[0]
                while sexo not in 'FM':
                    print('OPÇÃO INVÁLIDA!', end='')
        else:
            option = ' '
            while option not in 'SN':
                option = input(txt).strip().upper()[0]
                while option not in 'SN':
                    print('OPÇÃO INVÁLIDA!', end='')
            if option == 'N':
                break



valid('Digite seu : ')
valid('Deseja continuar?[S/N]: ')