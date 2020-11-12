km = float(input('Digite a distância em km da sua viagem: '))
viagens_curtas = (km * 0.50)
viagens_longas = (km * 0.45)
if km <= 200:
    print(f'Sua passagem sairá no valor de R${viagens_curtas} ')
else:
    print(f'Sua viagem sairá no valor de R${viagens_longas}')
