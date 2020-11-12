times = ('Fluminense', 'Corinthians', 'Flamengo', 'Atlético-MG', 'Coritiba', 'Sport Recife', 'Grêmio', 'Goiás', 'São Paulo', 'Botafogo', 'Bragantino',
         'Ceará', 'Bahia', 'Internacional', 'Athletico-PR', 'Palmeiras', 'Vasco da Gama', 'Atlético GO', 'Santos', 'Fortaleza')

#Tuplas imutáveis
print('-='*30)
print(f'Lista de times do Brasileirão: {times}')
print('-='*30)
print(f'Os 5 primeiros times são: {times[:5]}')
print('-='*30)
print(f'Os  últimos são: {times[-4:]}') #ou 16:
print('-='*30)
print(f'Times em ordem alfabética: {sorted(times)}') #Não afeta a tupla.
print('-='*30)
print(f'O palmeiras está na {times.index("Palmeiras")+1}ª posição')