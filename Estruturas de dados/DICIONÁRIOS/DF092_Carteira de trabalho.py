def header(txt):
    print('=' * 30)
    print(f'{"D A D O S":^30}')
    print('=' * 30)


from datetime import datetime
from time import sleep
dados = {}
dados['nome'] = input('Nome: ')
ano = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - ano
dados['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Salário: '))
    dados['aposentadoria'] = dados['idade'] + (dados['contratação'] - datetime.now().year + 35)
    sleep(1.5)
header('')
for key, value in dados.items():
    print(f'{key} tem o valor de {value}')
    print('-' * 30)










