numero = int(input('Digite um número: '))
soma = 0
cont = 0
for i in range(1,numero+1):
   if numero % i == 0:
       soma += 1
if soma == 2:
    print(f'{numero} é primo')
else:
    print(f'{numero} Não é primo')
