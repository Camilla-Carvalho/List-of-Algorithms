numero = (int(input('Digite um número: ')),
          int(input('Digite outro número: ')),
          int(input('Digite mais número: ')),
          int(input('Digite o último número: ')))
print('-'*30)
print(f'O valor 9 apareceu {numero.count(9)} vezes')
if 3 in numero:
    print(f'O número três apareceu na posição {numero.index(3)+1}ª')
else:
    print('O valor três não foi digitado em nenhuma posição')
print('Os valores pares digitados foram: ', end='')
for i in numero:
    if i %2 == 0:
        print(i, end=' ')