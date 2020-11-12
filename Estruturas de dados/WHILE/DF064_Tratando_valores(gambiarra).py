
#Soma de vários valores com condição de parada
value = soma = cont = 0
while value != 999:
    value = int(input('Digite um número [999 para parar]: '))
    if value != 999:
        soma += value
        cont += 1
    else:
        soma += value
        cont += 1
        print(f'Você digitou {cont - 1} números e a soma entre eles foi {soma - 999}.')
print('Acabou')

#Não fazer desta forma pois a variável soma estará com o valor errado