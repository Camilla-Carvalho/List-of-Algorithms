nome = str(input('Digite seu nome: ')).strip()
print('Analisando seu nome... ')
print(f'Seu nome com letras maiúsculas é: {nome.upper()}')
print(f'Seu nome com letras minúsculas é {nome.lower()}')
print('Seu nome tem ', len(nome) - nome.count(' '), 'letras')
partes_do_nome = (nome.split())
print(f'Seu primeiro nome é {partes_do_nome[0]} e ele tem {len(partes_do_nome[0])} letras')

