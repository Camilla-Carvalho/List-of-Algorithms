def cabeçalho(txt):
    print('='*30)
    print(f'{"T E L A":^30}')
    print('='*30)

aprovado = reprovado = 0
tela = {}
tela['nome'] = input('Nome: ').capitalize()
tela['media'] = float(input(f'Média de {tela["nome"]}: '))
if tela['media'] >= 7:
    tela['Situação'] = 'Aprovado'
else:
    tela['Situção'] = 'Recuperação'
print()
cabeçalho('')
for key, value in tela.items():
    print(f'{key} é igual a {value}')