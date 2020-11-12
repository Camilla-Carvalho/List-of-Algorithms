def header(txt):
    print('='* len(txt))
    print(f'{txt}')
    print('=' * len(txt))


cadastro = {}
pessoas = []
soma = media = 0
header(f'{"C A D A S T R O":^30}')
while True:
    cadastro.clear()
    cadastro['nome'] = input('Nome: ')
    while True:
        cadastro['sexo'] = input('Sexo: ').strip().upper()[0]
        if cadastro['sexo'] in 'FM':
            break
        print('ERRO! Digite apenas F ou M.')
    cadastro['idade'] = int(input('Idade: '))
    pessoas.append(cadastro.copy())
    soma += cadastro['idade']
    while True:
        option = input('Quer continuar?[S/N]: ').strip().upper()[0]
        if option in 'SN':
            print('-' * 30)
            break
        print('ERRO! Digite apenas S ou N.')
    if option == 'N':
        break

print(f'A) Ao todo temos {len(pessoas)} pessoas cadastradas')
media = (soma) / len(pessoas)
print(f'B) A média de idade é de {media:.2f} anos.')
print('C) As mulheres cadastradas foram: ', end='')
for pessoa in pessoas:
    if pessoa['sexo'] == 'F':
        print(f'{pessoa["nome"]} ', end='')
print('\nLista de pessoas que estão acima da média: \n', end='')
for pessoa in pessoas:
    if pessoa['idade'] >= media:
        print('     ', end='')
        for key, value in pessoa.items():
            print(f'{key} = {value}; ', end='')
        print()
print('<< FINISHED >>')





