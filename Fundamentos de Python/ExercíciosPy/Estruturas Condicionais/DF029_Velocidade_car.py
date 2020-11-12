velocidade = float(input('Digite a celocidade atal do carro: '))
if velocidade > 80:
    print('Você está dirigindo muito rápido')
    multa = ((velocidade - 80)*7)
    print(f'Você deverá pagar uma mula de R$ {multa:.2f} reais.')
print('Tenha um bom dia!  Dirija com segurança')