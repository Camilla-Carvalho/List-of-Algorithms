tupla = ('Fluminense', 'Corinthians', 'Flamengo', 'Atlético-MG', 'Coritiba', 'Sport Recife', 'Grêmio', 'Goiás', 'São Paulo', 'Botafogo', 'Bragantino',
         'Ceará', 'Bahia', 'Internacional', 'Athletico-PR', 'Palmeiras', 'Vasco da Gama', 'Atlético GO', 'Santos', 'Fortaleza')

print(f'\nOs cinco primeiros colocados são: {tupla[:5]}\n\nOs quatro umtimos colocados são {tupla[16:]}\n')
print(sorted(tupla))
print(count('Coritiba'))