def linha(lin):
    print('-'*30)

def cadastro(txt):
    linha('')
    print('\033[35mCADASTRO DE PESSOAS\033[0m')
    linha('')



idade = option = pessoas_maior_idade = homens = mulheres_menor_idade = 0
while True:
    cadastro('')
    sexo = ' '
    idade = int(input('Digite sua idade: '))
    sexo = input('Digte seu sexo [F/M]: ').strip().upper()[0]
    linha('')

    while sexo not in 'fFmM':
        sexo = input('\033[31mOPÇAO INVALIDA!Por favor digite seu sexo:\033[0m  ').strip().upper()[0]
        linha('')

    option = input('Deseja continuar? [S/N]: ').strip().upper()[0]
    while option not in 'SsNn':
        option = input('\033[31mOPÇAO INVALIDA! Deseja continuar? [S/N]: \033[0m').strip().upper()[0]

    if sexo in 'Ff' and idade < 20:
        mulheres_menor_idade += 1

    if sexo in 'Mm':            #Erro de identação
        homens += 1

    if idade <= 18:
        pessoas_maior_idade += 1

    if option == 'N':
        print('\n==========FIM DO PROGRAMA==========\n')
        break
print(f'Total de pessoas com mais de 18 anos: {pessoas_maior_idade}\n Ao todo temos {homens} homens cadastrados \n ', end='')
print(f'E temos  {mulheres_menor_idade} mulheres com menos de 20 anos')








