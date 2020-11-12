nome = str(input('Digite seu nome comleto: ')).strip()
nome_comp = (nome.split())
print(f'Seu primeiro nome é: {nome_comp[0]} ', end=' ')
print('e seu último nome é: {}'.format(nome_comp[len(nome_comp)-1]))


