from datetime import date
ano = date.today().year
maior = 0
menor = 0
for i in range(1,8):
    nascimento = int(input(f'Em que ano a {i}ª pessoa nasceu: '))
    idade = (ano - nascimento)
    if idade >= 18:
        maior += 1   #maior = maior + 1
    else:
        menor += 1 #Contador
print(f'\n\nAo todo {maior} pessoas são maior de idade\nE {menor} pessoas são menor de idade')




