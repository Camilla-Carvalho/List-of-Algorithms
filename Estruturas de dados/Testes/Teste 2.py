idade = [18, 29, 26, 32, 18]
pessoas = ['Laura', 'Diego', 'Leando', 'Evandro', 'Camilla']
pessoas.append(idade[:]) #Copia de dados
etnia = ['Negro', 'Branco', 'Pardo', 'Amarelo', 'Vermelho']
etnia.append(pessoas[:])
print(f'Etnia: {etnia}\nPessoas: {pessoas}')
print(f'Etnia: {etnia[1]} {etnia[4]}')