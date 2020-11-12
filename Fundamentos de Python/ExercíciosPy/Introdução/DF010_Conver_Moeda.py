print('Conversão da moeda real para dólar')
moeda = float(input('Digite o valor em dinheiro que possui na carteira: R$'))
dolar = (moeda/5.48)
if moeda <= 10.96:
    print(f'Com R${moeda:.2f}, você poderá comprar R${dolar:.2f} dólar!')
else:
    print(f'Com R${moeda:.2f}, você poderá comprar R${dolar:.2f} dólares!')