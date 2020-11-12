def header(txt):
    print('=' * 30)
    print(f'{"C A D A S T R O":^30}')
    print('=' * 30)

cadastro = {}
lista = []
mulheres = []
maior_media = []
pessoas = soma = media = 0
header('')
while True:
    cadastro['nome'] = input('Nome: ')
    cadastro['sexo'] = ' '
    while cadastro['sexo'] not in 'FM':
        cadastro['sexo'] = input('Sexo: ').strip().upper()[0]
        if cadastro['sexo'] in 'F':
            mulheres.append(cadastro['nome'])
        if cadastro['sexo'] not in 'FM':
            print('ERRO! Por favor, digite apenas M ou F.')

    cadastro['idade'] = int(input('Idade: '))
    lista.append(cadastro['nome'])
    pessoas += 1
    soma += cadastro['idade']

    media = soma / pessoas
    if cadastro['idade'] > media:
        maior_media.append(cadastro.copy())

    option = ' '
    while option not in 'SN':
        option = input('Quer continuar?[S/N]: ').strip().upper()[0]
        if option not in 'SN':
            print('ERRO! Responda apenas S ou N.')
    if option == 'N':
        break
    print('-' * 30)
print(f'A) Ao todo temos {len(lista)} pessoas cadastradas')
print(f'B) A média de idade é de {media:.2f}')
print(f'C) As mulheres cadastradas são:', end='')

for i, value in enumerate(mulheres):
    print(f' {value}', end='')

print('\nLista de pessoas que estão acima da média: ')

for i in enumerate(maior_media):
    for key, value in enumerate(i):
        print(f'{key} = {value}')

