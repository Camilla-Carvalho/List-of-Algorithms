def linha(lin):
    print('-'*30)

def cabeçalho(txt):
    linha('')
    print('=====CADASTRE UMA PESSOA=====')
    linha('')
maior18 = homens = mulheres20 = 0
while True:
    cabeçalho('')
    idade = int(input('Digite sua idade: '))
    linha('')
    sexo = ' '
    sexo = input('Digite seu sexo [M/F]: ').strip().upper()[0]
    linha('')
    while sexo not in 'FM':
        sexo = input('\033[31mSexo inváido! Por favor digite seu sexo [M/F]\033[0m: ').strip().upper()[0]
        linha('')
    option = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    while option not in 'SN':
        option = str(input('\033[31mOPÇÃO INVÁLIDA! Deseja continuar? [S/N]: \33[0m')).strip().upper()[0]

    if idade >= 18:
        maior18 += 1

    if sexo == 'M':                 #Fazer comparação fora do laço.
        homens += 1

    if sexo == 'F' and idade < 20: #mulheres com menos de 20 anos
        mulheres20 += 1

        linha('')
    if option == 'N': #Fora do laço.
        break
print(f'Total de pessoas com mais de 18 anos: {maior18}\nAo todo temos {homens} homens cadastrados')
print(f'Totala de mulheres com mais de 20 anos: {mulheres20}')