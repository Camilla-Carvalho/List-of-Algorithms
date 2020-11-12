sexo = input('Informe seu sexo [F/M]: ').strip().upper()[0]
while sexo not in 'FfMm':
    sexo = input('Dados inválidos! Por favor digite seu sexo [F/M]: ')
print('Dados cadastrados com sucesso!')

