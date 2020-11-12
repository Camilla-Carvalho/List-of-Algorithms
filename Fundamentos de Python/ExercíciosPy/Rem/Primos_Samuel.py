numero = int(input('Dgite um número: '))
cont = 0
i = 0
for i in range(0, numero, 2):
    if cont == i % 2 == 0:
        i += 1
        print(i)

