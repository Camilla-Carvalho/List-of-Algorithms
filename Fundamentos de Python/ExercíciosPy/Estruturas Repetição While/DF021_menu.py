value =  int(input('type a fist value: '))
value2 = int(input('type a second value: '))


print('''' MENU
[ 1 ] SOMAR
[ 2 ] MULTIPLICAR
[ 3 ] MAIOR
[ 4 ] NOVOS NÙMEROS
[ 5 ] SAIR DO PROGRAMA
''')
option = int(input('Type a option: '))
if option == 1:
    soma = (value + value2)
    print(soma)
elif option == 2:
    mult = (value * value2)
    print(mult)
elif option == 4:
    num = ('Deseja digitar novos números? [S/N]: ')
    if num in 'Ff' or num in 'Nn':

