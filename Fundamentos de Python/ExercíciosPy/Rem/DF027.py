nome = str(input('Digite seu nome completo: ')).strip()
partes_do_nome = (nome.split())
print(f'Muito prazer em te conhecer {partes_do_nome[0]}!')
print(f'Seu primeiro nome é {partes_do_nome[0]} e seu último nome é {partes_do_nome[len(partes_do_nome)-1]}')