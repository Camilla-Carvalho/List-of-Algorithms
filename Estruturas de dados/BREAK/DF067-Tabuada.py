def linha(lin):
    print('-'*50)


i = formula = num = 0
while True:
    linha('')
    num = int(input('Digite o numero que deseja consultar: '))
    for i in range(0, 10):
        if num > 0:
            i += 1
            formula = (num * i)
            print(f'{num} x {i} = {formula}')
    if num < 0:
        print('PROGRAMA DE TABUADA ENCERRADO.\nVolte Sempre!')
        break




