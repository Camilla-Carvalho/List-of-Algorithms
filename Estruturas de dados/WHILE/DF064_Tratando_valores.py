def inicio(txt):
    print('~'*30)
    print('TRATANDO VÁRIOS VALORES')
    print('~' * 30)


inicio('')
num = cont = soma = 0
num = int(input('Digite um número [999 para sair]: '))
while num != 999:
    cont += 1
    soma += num
    num = int(input('Digite um número [999 para sair]: '))
#Se eu ler o flag do lado de fora e do lado de dentro... automaticamente o 999 será desconsiderado como número da somatória
print(f'você digitou {cont} números e a soma entre eles é {soma}')