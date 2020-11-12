salario = float(input('Digite o valor do seu salário: '))
aumento1 = (salario * 10) / 100
aumento2 = (salario * 15) / 100

if salario <= 1250.00:
    print(f'Seu aumento será de R$\033[34m{aumento2:.2f} \033[0mreais,'
          f' totalizando no valor de R$\033[34m{aumento2+salario}\033[0m reais.')
if salario > 1250.00:
    print(f'Seu aumento será de R$\033[34m{aumento1:.2f}\033[0m reais,'
          f' totalizando no valor de R$\033[34m{aumento1+salario}\033[0m reais')
