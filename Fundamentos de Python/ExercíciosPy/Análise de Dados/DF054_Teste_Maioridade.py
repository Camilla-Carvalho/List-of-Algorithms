from datetime import date
ano = date.today().year
maior = 0
menor = 0
for i in range(1, 6+1):
    nascimento = int(input(f'Digite a data de nascimeto da {i}ª pessoa: '))
    idade = (ano - nascimento)
    if idade <= 18:
        menor += 1
    else:
        maior += 1 #identação
print(f'{maior} pessoas são de maior e {menor} são de menor')