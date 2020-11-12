from datetime import date
ano = date.today().year
maior = 0
menor = 0
for i in range(1,8):
    nascimento = int(input(f'Em que ano a {i}ª pessoa nasceu: '))
    idade = (ano - nascimento)
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print(f'Neste grupo há {maior} pessoas maiores de idade e {menor} pessoas menores de idade')


