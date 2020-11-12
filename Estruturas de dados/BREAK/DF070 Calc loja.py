def linha(txt):
    print('-'*30)

linha('')
print('LOJA SUPER BARATÂO')
linha('')
soma = mais_de_mil = 0
while True:
    produto = input('Digite o nome do produto: ')
    preço = float(input('DIgite o valor do produto R$:'))
    soma += preço
    option = ' '
    option = input('Deseja continuar?[S/N] ').strip().upper()[0]
    while option not in 'SN':
        option = input('\033[31mOPÇÂO INVÀLIDA! Deseja continuar?[S/N] \033[0m').strip().upper()[0]
    while option not in 'SN':
        produto = input('Digite o nome do produto: ')
        preço = float(input('DIgite o valor do produto R$:'))
        soma += preço
        option = input('Deseja continuar?[S/N] ').strip().upper()[0]

    if preço > 1000:
        mais_de_mil += 1

    if option == 'N':
        print('Fim do programa! ')
        break
print(f'O total da compra foi R${soma} reais')
print(f'Temos {mais_de_mil} produto custando mais de R$1.000 reais')

