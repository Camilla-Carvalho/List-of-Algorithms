import random
n1 = input('Digite o nome do primeiro aluno: ')
n2 = input('Digite o nome do segundo aluno: ')
n3 = input('Digite o nome do terceiro aluno: ')
n4 = input('Digite o nome do quarto aluno: ')
lista = [n1,n2,n3,n4]
#Listas no python são recohecidas com colchetes
escolhido = random.choice(lista)
print(f'O aluno escolhido foi {escolhido}')