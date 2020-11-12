from datetime import date
nascimento = int(input('Digite seu ano de nascimento: '))
sexo = input('Digite seu sexo: ')

ano_atual = date.today().year
idade = (ano_atual - nascimento)
if sexo.lower() == 'masculino' and idade < 18:

    print(f'\nVocê tem {idade} anos! ainda faltam {18 - idade} ano(s) para o alistamento... ')
    print(f'Seu tempo de alistamento será no ano de {ano_atual + (18 - idade)}')

elif sexo.lower() == 'masculino' and idade > 18:

   print(f'\nVocê tem {idade} anos e deveria ter se alistado há {idade- 18} ano(s)')
   print(f'Seu alistamento foi no ano de {ano_atual - (idade - 18)}')

elif sexo.lower() == 'masculino' and idade == 18:
   print('\nVocê deve se alistar IMEDIATAMENTE!')

elif sexo.lower() == 'feminino':
    print('Você infelizmente não pode se alistar :(')





