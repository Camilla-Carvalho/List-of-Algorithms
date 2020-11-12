print('Calculo do valor a pagar pelo aluguel de um carro')
dias = int(input('Digite por quantos dias o carro foi alugado: '))
km = float(input('Informe a quantidade de km rodado: '))
diasap = (dias * 60)
kmp = (km * 0.15)
total = (diasap + kmp)
print(f'O valor total a pagar é R${total:.2f}')
# Dividir para conquistar
# Exercícios com resltados muito grandes, devem ser quebrados em pedaços
# Dividir o programa em pequenos modulos.
