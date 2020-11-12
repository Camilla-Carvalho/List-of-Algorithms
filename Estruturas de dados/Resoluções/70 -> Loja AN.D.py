total = totmil = menor = cont = 0
barato = ''
while True:
    produto = str(input('Digite o nome do produto: '))
    preço = float(input('Digite o preço: R$'))
    cont += 1
    total += preço

    if preço > 1000:
        totmil += 1

    if cont == 1 or preço < menor:  # 1 == primeiro produto
        menor = preço
        barato = produto
#    else:
#        if preço < menor:
#            menor = preço
#            barato = produto

    resposta = ' '                                          #A comparação deve ser feita antes do laço while
    while resposta not in 'SN':
        resposta = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]

    if resposta == 'N':
        break

print(f'O total da compra foi R${total:.2f}\nTemos {totmil} produtos custando mais de R$1.000 reais') #Dois pontos
print(f'O produto mais barato foi {barato} custa R${menor:.2f}')
print('====================FIM DO PROGRAMA====================') #{:=eleva40} .format('Fim do programa')