def linha(lin):
    print('-'*40)

while True:
    linha('')
    num = int(input('Digite o número que deseja consultar: '))
    linha('')
    if num < 0:
        break
    for i in range(0, 10):
        i += 1
        print(f'{num} x {i} = {num * i}')
print('FIM DO PROGRAMA. Volte sempre!')
