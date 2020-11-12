n1 = float(input('Primeira prova: '))
n2 = float(input('Segunda nota: '))

media = (n1 + n2 ) / 2
print(f'Tirando {n1} e {n2}, sua média final foi {media}')

if media < 5:
    print('\033[31m \nREPROVADO')
elif media >= 7:
    print('\033[34m \nAPROVADO')

elif media >= 5 and media < 7:  # if 7 < media >= 5:
    print('\033[32m \nRECUPERAÇÃO')
