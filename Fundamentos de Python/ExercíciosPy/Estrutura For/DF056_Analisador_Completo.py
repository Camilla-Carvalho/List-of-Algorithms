from datetime import date
ano = date.today().year
soma_idade = 0
mais_velho = 0
nome_velho = 0
cont = 0
for i in range(1,5):
    print(f'-----{i}ª PESSOA-----')
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').strip()
    soma_idade += idade
    media_idade = (soma_idade/4)
   #if i == 1 and sexo in 'Mm'
    if i == 1 and sexo.upper() == 'M':
        mais_velho = idade
        nome_velho = nome
    if sexo.upper() == 'M' and idade > mais_velho:
        mais_velho = idade
        nome_velho = nome
#   if i == 1 and sexo in 'Ff':
#       mais_nova += idade
    if sexo in 'Ff' and idade <= 20:
        cont += 1

print(f'A media de idade do grupo é {media_idade} anos\nO homem mais velho tem {mais_velho} anos e', end=' ')
print(f'seu nome é {nome_velho}\nE há {cont} mulheres com menos de 20 anos no grupo.')
