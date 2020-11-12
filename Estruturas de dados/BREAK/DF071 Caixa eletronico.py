def cabeçalho(txt):
    print('='*40)
    print('{:^40}'.format('BANCO CEV'))
    print('='*40)

cabeçalho('')
saque = int(input('Digite o valor que deseja sacar: R$'))
total = saque
cedula = 50
total_cedulas = 0
while True:
    if total >= cedula:      #Se o valor for menor que o valor socilitado
        total -= cedula        # ele tira uma cédula de 50
        total_cedulas += 1      #E vai contar quantas notas de 50 precisa tirar
    else:
        if total_cedulas > 0:
            print(f'O total de cédulas é {total_cedulas} de R${cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
            total_cedulas = 0
        if total == 0:
            break