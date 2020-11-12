soma_idade = 0
media = 0
mais_velho_n = 0
mais_velho_i = 0
cont = 0

for i in range(1,5):
    print(f'-----{i}ª PESSOA-----')
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [F/M]: '))
    soma_idade += idade
    media = soma_idade/4
    if i == 1 and sexo.upper() == 'M':
        mais_velho_i = idade
        mais_velho_n = nome
    if sexo.upper() == 'M' and idade > mais_velho_i: #Erro de identação faz a diferença.
        mais_velho_i = idade
        mais_velho_n = nome
    if sexo in 'Ff' and idade <= 20:
        cont += 1

print(f'A média de idade do grupo é {media}\nO homem mais velho tem {mais_velho_i} anos e se chama {mais_velho_n}', end=' ')
print(f'E ao todo há {cont} mulheres com menos de 20 anos no grupo.')