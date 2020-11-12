import moeda
# from moeda import netade, dobro, aumentar


preço = float(input('Digite o preço: R$'))
print(f'A metade de R${preço} é R${moeda.metade(preço)}')
print(f'O dobro de R${preço:} é R${moeda.dobro(preço)}')
print(f'Aumentando 10%, temos R${moeda.porcentagem(preço, 10)}')
print(f'Reduzindo 13% temos R${moeda.diminuir(preço, 13)}')

