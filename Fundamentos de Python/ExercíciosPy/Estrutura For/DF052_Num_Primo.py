numero = int(input('Digite um número: '))
soma = 0
for i in range(1, numero + 1):
    if numero % i == 0:
        print(f'\033[34m{i}', end=' ')
        soma += 1
    else:
         print(f'\033[31m{i}', end=' ')
if soma == 2:
    print(f'\nO número {numero} é PRIMO!')
else:
    print(f'\n\n\033[31mO numero {numero} é divisível por {soma} números.. Ele NÂO é primo')


