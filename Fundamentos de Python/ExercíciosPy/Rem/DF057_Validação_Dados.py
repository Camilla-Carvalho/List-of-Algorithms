sexo = str(input('Informe seu sexo [F/M]: ')).strip()
i = True
while i == False:
    if sexo in 'MmFf':
        print('Sexo cadastrado com sucesso!')
    else:
        print('Sexo inválido, tente novamente')