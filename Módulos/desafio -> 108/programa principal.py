import moeda
# from moeda import netade, dobro, aumentar


preço = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(preço)} é {moeda.moeda(moeda.metade(preço))}') #moeda chamando a função moeda passando preço no parametro moeda
print(f'O dobro de {moeda.moeda(preço)} é {moeda.moeda(moeda.dobro(preço))}')
print(f'Aumentando 10%, temos {moeda.moeda(moeda.porcentagem(preço, 10))}')
print(f'Reduzindo 13% temos {moeda.moeda(moeda.diminuir(preço, 13))}')

