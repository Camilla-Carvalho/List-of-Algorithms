# teste = []
# teste.append('Camilla')
# teste.append(18)
# galera = list()
# galera.append(teste)
# teste[0] = 'Maria'
# teste[1] = 22
# galera.append(teste) #Listas copiadas tem uma ligação. Para que possamos copiar uma lista sem efeito eseplho
# print(galera) #É necessário usar [:] para que as listas não possuir ligação.

# galera = [['João', 19], ['Ana', 33], ['Maria', 45], ['Joaquim', 13]]
# galera.sort()
# print(galera[2][0])
#
# for pessoa in galera:
#     print(f'{pessoa[0]} tem {pessoa[1]} anos de idade')

galera = []
dados = list()
maior = menor = 0
for i in range(0, 3):
    dados.append(input('Nome: '))
    dados.append(int(input('Idade: ')))
    galera.append(dados[:])
    dados.clear()
for pessoa in galera:
    if pessoa[1] >= 21:
        print(f'{pessoa[0]} é maior de idade')
        maior += 1
    else:
        print(f'{pessoa[0]} é menor de idade')
        menor += 1
print(f'Este grupo tem {maior} pessoas maior de idade e {menor} pessoas menor de idade')
