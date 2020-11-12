peso = float(input('Digite o peso: (kg) '))
altura = float(input('Digite a sua altura: '))
imc = peso / (altura ** 2)
print(f'Seu imc é de {imc:.1f}')
if imc < 18.5:
    print('\033[31mVocê está abaixo do peso normal')
elif 18.5 <= imc < 25:
    print('\033[34m Você está no peso ideal!')
elif 25 <= imc < 30:
    print('\033[31m Você está em sobrepeso!')
elif 30 <= imc < 40:
    print('Obesidade')
else:
    print('Obesidade mórbida, Cuidado!')