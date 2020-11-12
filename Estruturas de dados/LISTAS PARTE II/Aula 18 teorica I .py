dados = list()
cabelo =[]
pessoas = list()

for i in range(0, 3):
    dados.append(input('Digite o nome: '))
    dados.append(int(input('Digite a idade: ')))
    cabelo.append(input('Digite o tpo do cabelo: '))


print(dados)
pessoas.append(dados[:]) ##Cópia de dados
pessoas.append(cabelo[:])
print(pessoas)

print(pessoas[1]) #A cópia de dados irá armazenar a cópia no primeiro índice da lista

##Cada lista é armazenada em seu respectivo índice