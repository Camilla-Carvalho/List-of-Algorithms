
valor = i = soma = 0
valor = int(input('Digite um valor [999 para sair]: '))
while valor != 999:
    i += 1
    soma += valor
    valor = int(input('Digite um valor [999 para sair]: '))
print(f'Você digitou {i} valores e a soma de todos foi {soma}')
