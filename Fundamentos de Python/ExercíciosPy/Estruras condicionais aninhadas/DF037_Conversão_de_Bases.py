numero = int(input('Digite o valor que deseja converter: '))
print('\033[034m=\033[0m'*40)
print('''
[ 1 ] BINÁRIO 
[ 2 ] OCTAL
[ 3 ] HEXADECIMAL\n''')

option = int(input('Digite a opção desejada: '))
print('\033[034m=\033[0m'*40)
if option == 1:
    print(f'{numero} convertido pra BINÁRIO ficará \033[32m{bin(numero)[2:]}\033[0m')
elif option == 2:
    print(f'{numero} convertido para OCTAL ficará \033[32m{oct((numero))[2:]}\033[0m')
elif option == 3:
    print(f'{numero} convertido para HEXAECIMAL ficará \033[32m{hex(numero)[2:]}\033[0m')
else:
    print('\033[31mOpção inválida!')

