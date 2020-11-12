sexo = input('Digite o Sexo [F/M]: ').strip().upper()[0]
while sexo not in 'MmFf':
    sexo = input('Sexo inválido! Por favor digite o seu sexo [F/M]: ')
print(f'Sexo {sexo} cadastrado com sucesso')