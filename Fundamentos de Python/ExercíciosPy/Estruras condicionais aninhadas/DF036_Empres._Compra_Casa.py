valor_da_casa = float(input('Digite o valor da casa: R$'))
salario = float(input('Digite o seu salário: R$'))
anos_financiamento = int(input('Em quantos anos deseja financiar a casa? \n \n'))

prestacao = valor_da_casa / (anos_financiamento * 12)
valor_minimo = salario * 30 / 100

print('\033[35m=-\033[0m'*30)

print(f'para pagar esta casa de R${valor_da_casa:.2f} reais em {anos_financiamento} anos , suas parcelas sairão no', end='')
print(f' valor de R${prestacao:.2f} reais,\nsendo o valor mínimo da parcela R${valor_minimo:.2f} reais')

if prestacao <= valor_minimo:
    print('Empréstimo CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')




