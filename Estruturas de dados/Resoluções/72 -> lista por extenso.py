def linha(lin):
    print('-'*40)

tupla = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete','Dezoito', 'Dezenove', 'Vinte')
while True:
    numero = int(input('Digite um número: '))
    linha('')
    if  0 <= numero <= 20:
        print(f'Você digitou o número {tupla[numero]}')
        linha('')
    else:
        print('Número inválido!')

    option = ' '
    while option not in 'SN':
        option = input('Deseja continuar? [S/N] '). strip().upper()[0]
        linha('')
    if option in 'N':
        print('Fim do programa')
        break



