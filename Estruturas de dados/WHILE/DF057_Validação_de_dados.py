print('Trabalhando com validação de dados...')
sexo = str(input('Digite seu sexo [F/M]: ')).strip().upper()[0]
while sexo not in 'FfmM':
   sexo = input('Dados inválidos! Por favor digite seu sexo: ').strip().upper()[0]
print(f'Sexo {sexo} cadastrado com sucesso!')





 

