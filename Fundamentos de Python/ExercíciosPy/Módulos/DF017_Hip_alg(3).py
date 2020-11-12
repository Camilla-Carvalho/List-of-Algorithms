from math import hypot
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o compimento do cateto adjacente: '))
hi = hypot(co,ca)
print(f'A hipotenusa será {hi:.2f}')
