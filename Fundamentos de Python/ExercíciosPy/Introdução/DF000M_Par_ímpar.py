print('Descobrindo se a soma de dois números é par ou ímpar')
a = int(input('Type a value any: '))
b = int(input('Type a other value any: '))
result = (a + b)
print(f'A soma entre {a} e {b} é {result}')
if (result % 2) == 0:
    print('Esse número é par')
else:
    print('Esse número é impar!')
