print('\033[36m{:=^40}'.format('LOJAS CARVALHO'))

preco = float(input('\033[0mDigite o valor total da compra: '))
print('''\nFORMAS DE PAGAMENTO
[ 1 ] À vista dinheiro/cheque
[ 2 ] À vista no cartão
[ 3 ] Em até 2X no cartão
[ 4 ] 3X no cartão ou mais\n''')

pagamento = int(input('tecle a opção de pagamento que deseja: '))

if pagamento == 1:
    desconto = (preco * 10) / 100
    print(f'\n\033[34mVocê terá 10% de desconto e sua compra de {preco:.2f} sairá no valor de R${preco - desconto:.2f}')

elif pagamento == 2:
    desconto = (preco * 5) / 100
    print(f'\n\033[34mVocê terá 5% de desconto e sua compra de {preco:.2f} sairá no valor de R${preco - desconto:.2f}')

elif pagamento == 3:
    print(f'\033[34m\nSua compra sairá no valor de R${preco:.2f}\033[0m')

elif pagamento == 4:

    juros = (preco * 20) / 100
    parcela = int(input('\nDigite a quantidade de parcelas: '))
    pagamento = (preco + juros) / parcela
    print(f'\n\033[34mSua compra será parcelada em {parcela:.2f}X de R${pagamento:.2f} com JUROS')
    print(f'Sua compra de R${preco:.2f} reais vai custar R${preco + juros:.2f} reais')
else:
    print('\n\033[31m OPÇÃO INVÁLIDA!')

