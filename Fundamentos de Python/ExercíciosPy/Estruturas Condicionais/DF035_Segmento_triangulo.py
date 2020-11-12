r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro Segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    print('\n\033[34mVocê pode formar um triangulo!')
else:
    print('\n\033[31mVocê não pode formar um triangulo!')