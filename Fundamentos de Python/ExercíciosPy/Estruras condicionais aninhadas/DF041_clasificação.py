from datetime import date
ano_nasc = int(input('Digite seu ano de nascimento: '))

ano_atual = date.today().year
idade= (ano_atual - ano_nasc)

print(f'O atleta tem {idade} ano(s)')

if idade < 9:
    print('Classficação: MIRIM')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Classificação: JUNIOR')
elif idade <= 25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')

