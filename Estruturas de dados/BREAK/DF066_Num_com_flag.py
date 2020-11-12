def cabecalho(txt):
    print('='*30)
    print('SOMA NÚMEROS COM FLAG')
    print('=' * 30)

i = soma = 0
cabecalho('')
while True:
    numero = int(input('Digite um número [999 para sair]: '))
    if numero == 999:
        break
    soma += numero
    i += 1
print(f'Você digitou {i} números e a soma de todos os números digitados foi: {soma}')



