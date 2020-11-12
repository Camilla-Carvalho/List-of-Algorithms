def header(txt):
    print('='*40)
    print(f'{"S I T U A Ç Ã O ":^40}')
    print('=' * 40)


tela = {}
tela['nome'] = input('Nome: ')
tela['media'] = float(input(f'Média de {tela["nome"]}: '))

if tela['media'] >= 7:
    tela['situacao'] = 'Aprovado'

elif tela['media'] >= 5 and tela['media'] < 7:
    tela['situacao'] = 'Recuperação'
else:
    tela['situacao'] = 'Reprovado'
header('')
for key, value in tela.items():
    print(f'{key} é igual a {value}')
print('-='*20)
print(f'{"F I N I S H E D":^40}')
print('-='*20)


